import subprocess
import datetime
import csv
import io
import requests
from xml.etree import ElementTree

from lksh.settings import EJUDGE_USER_LOGIN, EJUDGE_USER_PASSWORD, EJUDGE_CONTESTS_CMD_PATH, EJUDGE_SESSION_TIMEOUT, EJUDGE_NEW_MASTER

from libejudge.session import get_session


STATUS_STRINGS = {
    "OK": "OK",
    "CE": "Compilation Error",
    "RT": "Run-Time Error",
    "TL": "Time-Limit Exceeded",
    "PE": "Presentation Error",
    "WA": "Wrong Answer",
    "CF": "Check Failed",
    "PT": "Partial Solution",
    "AC": "Accepted for Testing",
    "IG": "Ignored",
    "DQ": "Disqualified",
    "PD": "Pending",
    "ML": "Memory Limit Exceeded",
    "SE": "Security Violation",
    "SV": "Style Violation",
    "WT": "Time-Limit Exceeded",
    "PR": "Pending Review",
    "RJ": "Rejected",
    "SK": "Skipped",
    "SY": "Synchronization Error",
    "SM": "Summoned for defence",

    "RU": "Running...",
    "CD": "Waiting...",
    "CG": "Compiling...",
    "AV": "Waiting...",
    "EM": "Empty record"
}


def run_contests_cmd(contest, action, *params):
    ssid = get_session(contest)
    try:
        output = subprocess.check_output([
            EJUDGE_CONTESTS_CMD_PATH,
            str(contest),
            action,
            "--session",
            ssid
        ] + list(map(str, params))).decode()
    except subprocess.CalledProcessError:
        return force_run_contests_cmd(contest, action, *params)
    return output

def force_run_contests_cmd(contest, action, *params):
    ssid = get_session(contest, force=True)
    try:
        output = subprocess.check_output([
            EJUDGE_CONTESTS_CMD_PATH,
            str(contest),
            action,
            "--session",
            ssid
        ] + list(map(str, params))).decode()
    except subprocess.CalledProcessError:
        return None
    return output


def get_run_info(contest, run_id):
    """
    Return dict with run information:
        size - size in bytes
        compiler - compiler short name
        verdict - two letter verdict
        verbose_verdict - full English verdict name
        score_info - scoring info, usually failed test
        problem - problem name
        id - run id

    :param run_id: int or str - run id
    :param contest: int - contest id
    :return: dict with info or None on failure
    """
    scsv = run_contests_cmd(contest, "run-status", run_id)
    if scsv is None:
        return None

    f = io.StringIO(scsv)
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        if int(row[0]) == int(run_id):
            size = int(row[3])
            problem = row[4]
            compiler = row[5]
            verdict = row[6]
            verbose_verdict = STATUS_STRINGS.get(row[6], row[6])
            try:
                score = int(row[7])
            except ValueError:
                score = None
            return {
                "size": size,
                "problem": problem,
                "compiler": compiler,
                "verdict": verdict,
                "verbose_verdict": verbose_verdict,
                "score": score,
                "id": int(run_id)
            }
    return None


def get_run_source(contest, run_id):
    """
    Return run source code
    :param run_id: int or str - run id
    :param contest: int - contest id
    :return: str - source code
    """
    source = run_contests_cmd(contest, "dump-source", run_id)
    return source


def get_compiler_log(contest, run_id):
    """
    Return compilation log for run
    :param run_id: int or str - run id
    :param contest: int - contest id
    :return: if compilation error occurred, log as str; None otherwise
    """
    sxml = run_contests_cmd(contest, "dump-report", run_id)
    if sxml is None:
        return None
    xml = "\n".join(sxml.split("\n")[2:])
    f = io.StringIO(xml)
    tree = ElementTree.parse(f)
    if tree.getroot().get('compile-error', 'no') == "yes":
        el = tree.findall('compiler_output')
        if el:
            return el[0].text
    return None


def submit_run(contest, problem_name, compiler, filename):
    """
    Submit run for checking
    :param contest: int - contest id
    :param problem_name: short problem name
    :param compiler: short compiler name
    :param filename: filename with source
    :return: int - run id
    """
    res = run_contests_cmd(contest, "submit-run", problem_name, compiler, filename)
    try:
        return int(res)
    except ValueError:
        return None


def get_available_compilers(contest):
    """
    Get available compilers as dict: short name -> long name
    :param contest: int - contest id
    :return: dict or None on failure
    """
    scsv = run_contests_cmd(contest, "dump-languages")
    if scsv is None:
        return None

    f = io.StringIO(scsv)
    reader = csv.reader(f, delimiter=';')
    res = {}
    for row in reader:
        res[row[1]] = row[2]
    return res


def get_contest_status(contest):
    # "not running", "running", "paused", "over"
    res = run_contests_cmd(contest, "get-contest-status")
    return res


def reset_contest(contest):
    ssid = get_session(contest)
    sid, clkey = ssid.split('-')
    requests.post(EJUDGE_NEW_MASTER, data={"SID": sid, "action_115": "Reset the contest!!!"}, cookies={"EJSID": clkey})


def is_upsolving(contest):
    ssid = get_session(contest)
    sid, clkey = ssid.split('-')
    return "Upsolving mode" in requests.get(EJUDGE_NEW_MASTER, data={"SID": sid}, cookies={"EJSID": clkey}).text
