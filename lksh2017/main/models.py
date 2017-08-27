from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from libejudge import Userlist
import xml.etree.ElementTree as ET
from django.utils.translation import ugettext as _
from datetime import datetime
from libejudge.run import get_contest_status, run_contests_cmd
import uuid
import os.path
from django.utils.timezone import utc
from django.utils.safestring import mark_safe

def random_statement_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('statements', filename)


class User(AbstractBaseUser):
    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
    id = models.IntegerField(primary_key=True, help_text="ejudge user id",)
    bonuses = models.IntegerField("Бонусы", default=0)
    username = models.CharField("Логин", max_length=128, unique=True, null=True)
    groups = models.ManyToManyField("Group")

    email = ""
    is_active = True
    is_staff = False
    is_superuser = False
    full_name = "" # expected to be "LastName FirstName[ Patronymic]"

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.populate()

    def __str__(self):
        return self.get_full_name()

    def grouplist(self):
        return ", ".join([x.short_name for x in self.groups.all()])

    def populate(self):
        if not self.id:
            return
        clnt = Userlist()
        clnt.adminProcess()

        xml = ET.fromstring(clnt.privGetUserInfo(self.id, 0))
        if xml.attrib.get('privileged', 'no') == 'yes':
            self.is_staff = True
            self.is_superuser = True

        for tag in xml:
            if tag.tag == 'email':
                self.email = tag.text or ""
            if tag.tag == 'name':
                self.full_name = tag.text or ""
            if tag.tag == 'login':
                self.username = tag.text or ""
            if tag.tag == 'contests':
                ids = []
                for cnt in tag:
                    if cnt.attrib.get('status', 'none') == 'ok':
                        ids.append(cnt.attrib.get('id', 0))
                groups = Group.objects.filter(reg_contest__in=ids).all()
                if set([x.id for x in groups]) != set([x.id for x in self.groups.all()]):
                    self.groups.clear() 
                    for x in groups:
                        self.groups.add(x.id)


    def get_full_name(self):
        return self.full_name or self.username

    def get_short_name(self):
        try:
            return self.full_name.split()[1]
        except:
            return self.full_name or self.username

    def has_module_perms(self, app):
        return self.is_superuser and self.is_active

    def has_perm(self, perm, obj=None):
        return self.is_superuser and self.is_active

    def has_perms(self, perms, obj=None):
        return self.is_superuser and self.is_active

class EjudgeAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            clnt = Userlist()
            ip = request.META['REMOTE_ADDR'] or '0.0.0.0'
            res = clnt.login(ip, request.is_secure(), 0, -1, username, password)
            if not res:
                return None
            return self.get_user(res['user_id'])
        except:
            return None

    def get_user(self, user_id):
        if user_id < 1:
            return None
        try:
            created = False
            try:
                user = User.objects.get(pk=user_id)
            except:
                user = User()
                created = True
                user.id = user_id
                user.save()
                user.populate()        
                user.save()
            
            return user
        except:
            return None


class Group(models.Model):
    class Meta:
        verbose_name = "группа"
        verbose_name_plural = "группы"
    full_name = models.CharField("Полное название группы", max_length=128)
    short_name = models.CharField("Краткое название группы", max_length=128)
    standings = models.BooleanField("Показывать ссылку на сводную таблицу", default=True)
    reg_contest = models.IntegerField("Контест с участниками")
    casino_contest = models.IntegerField("Контест казино", default=0, help_text="ID контеста или 0, если такого нет")
    casino_statement = models.FileField("Файл с условием задачи для казино", upload_to=random_statement_path, null=True, blank=True)

    def __str__(self):
        return self.short_name


class Prize(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name = 'приз'
        verbose_name_plural = 'призы'
    name = models.CharField("Название", max_length=128, db_index=True)
    cost = models.IntegerField("Цена")
    description = models.TextField(default="", blank=True)
    stock = models.IntegerField("В наличии")
    picture = models.ImageField("Картинка", upload_to='prizes')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    class Meta:
        verbose_name = 'занятие'
        verbose_name_plural = 'занятия'
        ordering = ('group__short_name', 'date')
    name = models.CharField("Название", max_length=128, help_text="Например, \"Тренировка 01\"")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="lessons")
    contest_id = models.IntegerField("Контест в ejudge", default=0, help_text="ID контеста или 0, если такого нет")
    statement = models.FileField("Файл с условиями", upload_to=random_statement_path, null=True, blank=True)
    date = models.DateField()
    description = models.TextField(default="", blank=True)
    autorewards = models.TextField("Автонаграды", default="", blank=True, help_text=mark_safe('<a href="/static/rewards.html">Справка</a>'))
    bank = models.ForeignKey(User, help_text="С кого списываются баллы за автонаграды", null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(str(self.group), self.name)

    @property
    def url(self):
        return "/ejudge/web-client?contest_id={}".format(self.contest_id)

    @property
    def standings_url(self):
        return "/ejudge/%06d.html" % self.contest_id

    @property
    def contest_started(self):
        return (self.contest_id > 0) and (get_contest_status(self.contest_id) == "running")
        


class LessonAttachment(models.Model):
    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="attachments")
    name = models.CharField("Название", max_length=128, help_text="Например, \"План лекции\"")
    file = models.FileField("Файл", upload_to="lessons")

    def __str__(self):
        return self.name 


class Transaction(models.Model):
    class Meta:
        verbose_name = 'транзакция'
        verbose_name_plural = 'транзакции'
    sender = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True, related_name="sender")
    receiver = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True, related_name="receiver")
    amount = models.IntegerField(default=0)
    when = models.DateTimeField(auto_now=True)

    @property
    def description(self):
        if self.sender is None:
            if self.receiver is None:
                return "(невалидная транзакция)"
            else:
                return "{} получил(а) {} бонусов".format(self.receiver.username, self.amount)
        else:
            if self.receiver is None:
                return "{} потратил(а) {} бонусов".format(self.sender.username, self.amount)
            else:
                return "{} перевел(а) {} бонусов -> {}".format(self.sender.username, self.amount, self.receiver.username)
    
    def __str__(self):
        return "[{}] {}".format(datetime.strftime(self.when, "%c"), self.description)


class Purchase(models.Model):
    class Meta:
        verbose_name = 'покупка'
        verbose_name_plural = 'покупки'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchases")
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE, related_name="purchases")
    when = models.DateTimeField(auto_now=True)
    code = models.CharField("Код", max_length=8, unique=True)

    PAYED = "PD"
    RECEIVED = "RC"
    DECLINED = "DC"
    REFUNDED = "RF"
    STATUS = (
        (PAYED, "Оплачено"),
        (RECEIVED, "Получено"),
        (DECLINED, "Отклонено"),
        (REFUNDED, "Возвращено")
    )
    status = models.CharField("Статус", max_length=2, choices=STATUS, default=PAYED)

    @property
    def description(self):
        return "{} купил(а) {} - {}".format(self.user.get_full_name(), self.prize.name, self.get_status_display())
    
    def __str__(self):
        return "[{}] {}".format(datetime.strftime(self.when, "%c"), self.description)


class Autoreward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    prob = models.CharField(max_length=64, db_index=True)


# Casino settings
CHILL_TIME = 10
READ_TIME = 60
BET_TIME = 30

class CasinoSession(models.Model):
    class Meta:
        verbose_name = 'сессия в казино'
        verbose_name_plural = 'сессии в казино'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    bet = models.IntegerField("Ставка", default=0)
    time_bet = models.IntegerField("Ставка по времени", default=0)
    solved = models.BooleanField("Задача решена", default=False)
    solved_time = models.IntegerField("Время решения", default=0)
    start = models.DateTimeField("Начало сессии", auto_now_add=True)
    won = models.IntegerField("Выигрыш", default=0)

    def __str__(self):
        return self.group.short_name + " - " + self.user.get_full_name()

    @property
    def is_ok(self):
        return self.solved_time <= self.time_bet and self.solved

    @property
    def elapsed(self):
        return int((datetime.utcnow().replace(tzinfo=utc) - self.start).total_seconds())

    def start_contest(self):
        run_contests_cmd(self.group.casino_contest, "force-start-virtual", self.user.id)

    @property
    def status(self):
        elapsed = self.elapsed
        if elapsed < CHILL_TIME:
            return "chill"
        elapsed -= CHILL_TIME
        if elapsed < READ_TIME:
            return "read"
        elapsed -= READ_TIME
        if elapsed < BET_TIME:
            return "bet"
        return "solve"

    @property
    def next_refresh(self):
        elapsed = self.elapsed
        if elapsed < CHILL_TIME:
            return CHILL_TIME
        elapsed -= CHILL_TIME
        if elapsed < READ_TIME:
            return CHILL_TIME + READ_TIME
        elapsed -= READ_TIME
        if elapsed < BET_TIME:
            return CHILL_TIME + READ_TIME + BET_TIME
        return -CHILL_TIME - READ_TIME - BET_TIME

    @property
    def rank(self):
        if self.solved:
            if self.is_ok:
                return 0, self.time_bet
            else:
                return 1, self.solved_time
        else:
            return 2, 0

    @property
    def statement_visible(self):
        return self.elapsed >= CHILL_TIME

    @property
    def login_visible(self):
        return self.elapsed >= CHILL_TIME + READ_TIME + BET_TIME

    def refresh(self):
        if self.solved:
            return
        contest_id = self.group.casino_contest
        user_id = self.user.id
        data = run_contests_cmd(contest_id, "dump-filtered-runs", "user_id==%d && status == OK" % user_id, "0", "-1")
        if data:
            self.solved = True
            time = data.split(';')[5]
            x = time.split(' ')
            y = list(map(int, x[-1].split(':')))
            sec = y[2] + y[1] * 60 + y[0] * 3600
            if len(x) > 1:
                sec += 86400 * int(x[0])
            sec -= CHILL_TIME + READ_TIME + BET_TIME
            if sec < 0:
                sec = 0
            self.solved_time = sec
            self.save()
