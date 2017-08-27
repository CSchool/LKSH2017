import subprocess
import datetime

from lksh.settings import EJUDGE_USER_LOGIN, EJUDGE_USER_PASSWORD, EJUDGE_CONTESTS_CMD_PATH, EJUDGE_SESSION_TIMEOUT

cached_session_id = {}
cached_session_time = {} 


def do_subprocess(contest):
    global cached_session_time, cached_session_id
    try:
        cached_session_id[contest] = subprocess.check_output((
            EJUDGE_CONTESTS_CMD_PATH,
            str(contest),
            "master-login",
            "STDOUT",
            EJUDGE_USER_LOGIN,
            EJUDGE_USER_PASSWORD
        ))
        cached_session_id[contest] = cached_session_id.decode().strip()
    except:
        return False
    return True


def do_libejudge(contest):
    global cached_session_time, cached_session_id
    try:
        import libejudge 
        clnt = libejudge.Userlist()
        r = clnt.privLogin('127.0.0.1', 0, contest, 0, 6, EJUDGE_USER_LOGIN, EJUDGE_USER_PASSWORD)
        cached_session_id[contest] = "%016x-%016x" % (r['sid'], r['client_key'])
    except:
        return False
    return True


def get_session(contest, force=False):
    global cached_session_time, cached_session_id
    if force or (cached_session_id.get(contest) is None or (datetime.datetime.now() - \
        cached_session_time[contest]).seconds > EJUDGE_SESSION_TIMEOUT):
        if not do_libejudge(contest):
            do_subprocess(contest)
        cached_session_time[contest] = datetime.datetime.now()
    return cached_session_id[contest]
