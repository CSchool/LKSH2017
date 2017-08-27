from main.models import Group, CasinoSession, Transaction
from lksh.settings import MEDIA_ROOT
import os.path
from libejudge.run import reset_contest

def render_casino(group):
    sessions = list(CasinoSession.objects.filter(group=group).all())
    sessions.sort(key=lambda x: x.rank)

    body = ""
    for session in sessions:
        session.refresh()
        status = session.status
        if status != "solve" or not session.solved:
            msg = "не решено"
            if status == "chill":
                msg = "ожидает начала"
            elif status == "read":
                msg = "читает условие"
            elif status == "bet":
                msg = "делает ставку"
            body += """
                    <tr class="{cl}">
                        <td>{team}</td>
                        <td>{bet}</td>
                        <td colspan="{cs}">
                            <b>{msg}</b>
                        </td>
                        {st}
                    </tr>""".format(cs=2 if session.won else 3, cl="pr" if status != "solve" else "fl", bet=session.bet,
                            team=session.user.get_full_name(), msg=msg, st='<td>{}</td>'.format(session.won) if session.won else '')
        else:
            body += """
                    <tr class="{cl}">
                        <td>{team}</td>
                        <td>{bet}</td>
                        <td>{time_bet}</td>
                        <td>{solved_time}</td>
                        <td>{won}</td>
                    </tr>""".format(cl="ok" if session.is_ok else "fl", team=session.user.get_full_name(), bet=session.bet,
                            time_bet=session.time_bet, solved_time=session.solved_time, won=session.won)

    return """<!doctype html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <link href="/ejudge/unpriv.css" type="text/css" rel="stylesheet" />
        <link href="/static/stand.css" type="text/css" rel="stylesheet" />
        <title>{group} - результаты казино</title>
    </head>
    <body>
        <h1>{group} - результаты казино</h1>
        <div class="table-wrapper">
            <table class="st">
                <thead>
                    <tr>
                        <th>Участник</th>
                        <th>Ставка (бонусы)</th>
                        <th>Ставка (время)</th>
                        <th>Время решения</th>
                        <th>Выигрыш (бонусы)</th>
                    </tr>
                </thead>
                <tbody>{body}
                </tbody>
            </table>
        </div>
    </body>
</html>
""".format(group=group, body=body)

def finalize_casino(group):
    sessions = list(CasinoSession.objects.filter(group=group).all())
    st = {}
    for s in sessions:
        st[s.id] = s
    sessions.sort(key=lambda x: x.bet)
    for i in range(len(sessions)):
        sessions[i].bank = sessions[i].bet
    for i in range(len(sessions)):
        sessions[i].pot_idx = [sessions[j].id for j in range(i + 1)]
        sessions[i].pot = sessions[i].bank * (len(sessions) - i)
        for j in range(i + 1, len(sessions)):
            sessions[j].bank -= sessions[i].bet
    sessions.sort(key=lambda x: x.rank)
    c = 1
    for i in range(len(sessions)):
        sessions[i].idx = i
    for i in range(1, len(sessions) + 1):
        if i == len(sessions) or sessions[i - 1].rank != sessions[i].rank:
            pot = [0] * len(sessions)
            cnt = [0] * len(sessions)
            for j in st:
                pot[st[j].idx] = st[j].pot
            for k in range(c):
                for j in sessions[i - 1 - k].pot_idx:
                    cnt[st[j].idx] += 1
            for k in range(len(sessions)):
                if cnt[k]:
                    pot[k] /= cnt[k]
            for k in range(c):
                for j in sessions[i - 1 - k].pot_idx:
                    st[j].pot = 0
            for j in range(c):
                sessions[i - 1 - j].won = 0
            for k in range(c):
                for j in sessions[i - 1 - k].pot_idx:
                    sessions[i - 1 - k].won += pot[st[j].idx]
            c = 1
        else:
            c += 1
    for s in sessions:
        s.won = int(s.won)
        s.save()

def close_casino(finalize=True):
    for group in Group.objects.all():
        if group.casino_contest:
            if finalize:
                finalize_casino(group)
            with open(os.path.join(MEDIA_ROOT, 'casino_%d.html' % group.id), "w") as f:
                f.write(render_casino(group))
    for session in CasinoSession.objects.all():
        if session.won:
            tr = Transaction()
            tr.receiver = session.user
            tr.amount = session.won
            tr.save()
            session.user.bonuses += session.won
            session.user.save()
    for group in Group.objects.all():
        if group.casino_contest:
            reset_contest(casino_contest)
    CasinoSession.objects.all().delete()
