from main.models import Lesson, Autoreward, EjudgeAuthBackend, User, Transaction
from libejudge.run import run_contests_cmd, is_upsolving


class Rule:
    problems = []
    score = 0
    add = False
    upsolving_yes = True
    upsolving_no = True
    contest_id = 0
    upsolving = False
    def __init__(self, upsolving, rule):
        self.upsolving = upsolving
        prob, _score = rule.split('=')
        if prob == '*':
            self.problems = '__all__'
        else:
            self.problems = prob.split(',')
        if ':' in _score:
            score, flags = _score.split(':')
        else:
            score, flags = _score, ""
        score = int(score)
        self.score = score
        self.add = 'a' in flags
        if 'u' in flags or 'U' in flags:
            self.upsolving_yes = 'U' in flags
            self.upsolving_no = 'u' in flags

    def appliable(self, prob):
        if self.upsolving and not self.upsolving_yes or not self.upsolving and not self.upsolving_no:
            return False
        if self.problems == '__all__':
            return True
        return prob in self.problems


def autoreward_lesson(lesson):
    if not lesson.contest_id:
        return
    upsolving = is_upsolving(lesson.contest_id)
    rules = [Rule(upsolving, rule) for rule in lesson.autorewards.split("\n")]
    runs = run_contests_cmd(lesson.contest_id, "dump-filtered-runs", "status==OK", "0", "-1").split('\n')
    for s in runs:
        if not s:
            continue
        info = s.split(';')
        user_id, prob = int(info[10]), info[18]
        if not Autoreward.objects.filter(user__id=user_id, prob=prob, lesson=lesson).exists():
            score = 0
            for rule in rules:
                if rule.appliable(prob):
                    score += rule.score
                    if not rule.add:
                        break
            r = Autoreward()
            r.user = EjudgeAuthBackend().get_user(user_id)
            r.prob = prob
            r.lesson = lesson
            r.save()
            if score > 0:
                r.user.bonuses += score
                r.user.save()
                lesson.bank.bonuses -= score
                tr = Transaction()
                tr.sender = lesson.bank
                tr.receiver = r.user
                tr.amount = score
                tr.save()
    lesson.bank.save()
