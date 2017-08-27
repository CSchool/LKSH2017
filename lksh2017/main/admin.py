from django.contrib import admin
from django.contrib.admin.helpers import ActionForm
from django import forms
from django.contrib.auth.models import Group as _Group
from django.utils.safestring import mark_safe
admin.site.unregister(_Group)

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


from main.models import User, Group, Prize, Lesson, LessonAttachment, Transaction, Purchase, CasinoSession

class GiveBonusesActionForm(ActionForm):
    bonuses = forms.IntegerField(label=mark_safe("&nbsp;&nbsp;Количество бонусов:&nbsp;"), required=True)

def give_bonuses(modeladmin, request, queryset):
    bonuses = int(request.POST['bonuses'])
    for user in queryset:
        user.bonuses += bonuses
        user.save()
        request.user.bonuses -= bonuses
        tr = Transaction()
        tr.sender = request.user
        tr.receiver = user
        tr.amount = bonuses
        tr.save()
    request.user.save()
give_bonuses.short_description = "Передать бонусы"

def add_bonuses(modeladmin, request, queryset):
    bonuses = int(request.POST['bonuses'])
    for user in queryset:
        user.bonuses += bonuses
        user.save()
        tr = Transaction()
        tr.receiver = user
        tr.amount = bonuses
        tr.save()
add_bonuses.short_description = "ДОБАВИТЬ бонусы"

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['username', 'id', 'full_name', 'email', 'groups', 'is_staff']
    fields = ['username', 'id', 'full_name', 'email', 'groups', 'is_staff', 'bonuses']
    list_display = ['__str__', 'bonuses', 'grouplist']
    list_filter = (('groups', custom_titled_filter('Группа')),)
    action_form = GiveBonusesActionForm
    actions = [give_bonuses, add_bonuses]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(User, UserAdmin)

class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ['standings_url']

    def standings_url(self, obj):
        if obj.id and obj.standings:
            return '<a href="/standings/%d"><b>Сводная таблица</b></a>' % obj.id
        return ''
    standings_url.allow_tags = True

admin.site.register(Group, GroupAdmin)

class PrizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'cost')

admin.site.register(Prize, PrizeAdmin)
admin.site.register(Transaction)

class LessonAttachmentInline(admin.TabularInline):
    model = LessonAttachment

class LessonAdmin(admin.ModelAdmin):
    inlines = [
        LessonAttachmentInline
    ]
    list_filter = (('group', custom_titled_filter('Группа')),)
    list_display = ('__str__', 'group')

admin.site.register(Lesson, LessonAdmin)

def make_received(modeladmin, request, queryset):
    queryset.update(status=Purchase.RECEIVED)
make_received.short_description = "Пометить покупки как полученные"

def make_declined(modeladmin, request, queryset):
    for purchase in queryset.all():
        purchase.user.bonuses += purchase.prize.cost
        purchase.user.save()
        purchase.prize.stock += 1
        purchase.prize.save()
        purchase.status = Purchase.DECLINED
        purchase.save()
        tr = Transaction()
        tr.receiver = purchase.user
        tr.amount = purchase.prize.cost
        tr.save()
make_declined.short_description = "Отклонить покупки"

class PurchaseAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('__str__', 'code', 'status')
    search_fields = ('code',)
    actions = (make_received, make_declined)

admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(CasinoSession)
