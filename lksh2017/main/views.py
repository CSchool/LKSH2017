from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from main.standings import render_standings
from main.casino import render_casino
from lksh.settings import STANDINGS_DIR
from main.models import Group, Prize, Purchase, Transaction, User, CasinoSession, Lesson
from main.autorewards import autoreward_lesson
import random
import string

import os.path

def index(req):
    if req.user.is_authenticated:
        prizes = Purchase.objects.filter(status=Purchase.PAYED, user=req.user).all()
    else:
        prizes = []
    if req.POST.get('action') == 'autoreward' and req.user.is_staff:
        try:
            lesson = Lesson.objects.get(id=req.POST.get('lesson_id'))
            autoreward_lesson(lesson)
            return redirect('/')
        except:
            raise Http404()
    if req.POST.get('action') == 'autoreward_group' and req.user.is_staff:
        try:
            group = Group.objects.get(id=req.POST.get('group_id'))
            for lesson in group.lessons.all():
                autoreward_lesson(lesson)
            return redirect('/')
        except:
            raise Http404()
    return render(req, 'index.html', context=dict(prizes=prizes))

def casino(req, group_id):
    session = False
    try:
        group = Group.objects.get(id=group_id)
        if CasinoSession.objects.filter(user=req.user, group=group).exists():
            session = True
        if not group.casino_contest:
            raise ValueError
        if not req.user.is_authenticated:
            raise ValueError
        if not User.objects.filter(id=req.user.id, groups__id=group.id).exists():
            raise ValueError
    except:
        raise Http404()
    if req.POST.get('action') == 'start' and not session:
        try:
            bet = int(req.POST.get('bet'))
            if bet < 0:
                raise ValueError
            if bet > req.user.bonuses:
                raise ValueError
            sess = CasinoSession()
            sess.group = group
            sess.user = req.user
            sess.bet = bet
            sess.save()
            sess.start_contest()
            transaction = Transaction()
            transaction.sender = req.user
            transaction.amount = bet
            transaction.save()
            req.user.bonuses -= bet
            req.user.save()
            return redirect('/casino/%d/play' % group.id)
        except:
            raise Http404()

    return render(req, 'casino.html', context=dict(group=group, session=session))

def casino_standings(req, group_id):
    try:
        group = Group.objects.get(id=group_id)
        if not req.user.is_staff:
            raise ValueError
        if not group.casino_contest:
            raise ValueError
        if not User.objects.filter(id=req.user.id, groups__id=group.id).exists():
            raise ValueError
    except:
        raise Http404()
    return HttpResponse(render_casino(group))

def casino_play(req, group_id):
    try:
        group = Group.objects.get(id=group_id)
        session = CasinoSession.objects.get(user=req.user, group=group)
        if not group.casino_contest:
            raise ValueError
        if not req.user.is_authenticated:
            raise ValueError
        if not User.objects.filter(id=req.user.id, groups__id=group.id).exists():
            raise ValueError
    except:
        raise Http404()
    session.refresh()
    if req.POST.get('action') == 'bet':
        try:
            bet = int(req.POST.get('bet'))
            if bet < 0:
                raise ValueError
            if bet > 7200:
                raise ValueError
            if session.status != "bet":
                raise ValueError
            session.time_bet = bet
            session.save()
        except:
            pass
    return render(req, 'casino_play.html', context=dict(group=group, session=session))

def standings(req, group_id):
    try:
        group = Group.objects.get(id=group_id)
    except:
        raise Http404()
    if not group or not group.standings:
        raise Http404()
    path = os.path.join(STANDINGS_DIR, 'group_%d.html' % group.id)
    stand = ""
    if not os.path.isfile(path):
        stand = render_standings(group)
        with open(path, 'w') as f:
            f.write(stand)
    else:
        with open(path, 'r') as f:
            stand = f.read()
    return HttpResponse(stand)

def prizes(req):
    if not req.user.is_authenticated:
        raise Http404()
    if req.POST.get('action') == 'purchase':
        try:
            prize = Prize.objects.get(id=req.POST.get('prize'))
            if prize.stock <= 0:
                raise ValueError("Not enough stock")
            if prize.cost > req.user.bonuses:
                raise ValueError("Too expensive")
            purchase = Purchase()
            purchase.user = req.user
            purchase.prize = prize
            purchase.code = ''.join(random.choice("ABCDEFGHKMNPQRSTUVWXYZ23456789") for _ in range(8))
            purchase.status = Purchase.PAYED
            purchase.save()
            transaction = Transaction()
            transaction.sender = req.user
            transaction.amount = prize.cost
            transaction.save()
            req.user.bonuses -= prize.cost
            req.user.save()
            prize.stock -= 1
            prize.save()
            return redirect('/')
        except:
            raise Http404()
    return render(req, 'prizes.html', context=dict(prizes=Prize.objects.filter(stock__gt=0).order_by('cost').all()))
