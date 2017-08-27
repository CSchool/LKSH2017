from main.models import Group
from html.parser import HTMLParser
import xml.etree.ElementTree as ET
from copy import deepcopy
from datetime import datetime

def get_path(contest):
    return "/home/judges/%06d/var/status/dir/standings.html" % contest

def get_contest_name(contest):
    path = "/home/judges/data/contests/%06d.xml" % contest
    with open(path, "r") as f:
        xml = ET.fromstring(f.read())

        for child in xml:
            if child.tag == "name":
                return child.text
    return "Unknown"

INACTIVE = 0
HEADER = 1
ROW = 2
TOTAL = 3
SUCCESS = 4
PERCENT = 5

PLACE = 1
TEAM = 2
PROBLEM = 3
SOLVED = 4
PENALTY = 5

READ_PROBLEM_NAME = 1
READ_TEAM = 2
READ_STATUS = 3
READ_PLACE = 4

class Parser(HTMLParser):
    status = INACTIVE
    column = INACTIVE
    data = INACTIVE
    problems = []
    problem = 0
    teams = []
    team = ""
    statuses = {}
    good = False
    cur_attrs = {}

    def init(self):
        self.status = INACTIVE
        self.column = INACTIVE
        self.data = INACTIVE
        self.problems = []
        self.problem = 0
        self.teams = []
        self.team = ""
        self.statuses = {}
        self.good = False
        self.cur_attrs = {}


    def handle_starttag(self, tag, attrs):
        if tag =="table":
            self.good = True
        elif tag == "tr":
            if self.status == INACTIVE:
                self.status = HEADER
            elif self.status == HEADER:
                self.status = ROW
            elif self.status == TOTAL:
                self.status = SUCCESS
            elif self.status == SUCCESS:
                self.status = PERCENT
            self.column = INACTIVE
        elif tag == "th" or tag == "td":
            if self.column == INACTIVE:
                self.column = PLACE
            elif self.column == PLACE:
                self.column = TEAM
            elif self.column == TEAM:
                self.column = PROBLEM
                self.problem = 0
            elif self.column == PROBLEM and self.status == ROW:
                self.problem += 1
                if self.problem >= len(self.problems):
                    self.column = SOLVED
            elif self.column == SOLVED:
                self.column = PENALTY
            if self.status == HEADER:
                if self.column == PROBLEM:
                    self.data = READ_PROBLEM_NAME
            if self.status == ROW:
                if self.column == PLACE:
                    self.data = READ_PLACE
                if self.column == TEAM:
                    self.data = READ_TEAM
                if self.column == PROBLEM:
                    self.cur_attrs = dict(attrs)
                    self.data = READ_STATUS

    def handle_endtag(self, tag):
        if tag == "th" or tag == "td":
            self.data = INACTIVE
        if tag == "tr":
            if self.status == HEADER:
                self.problems = self.problems[:-2]

    def handle_data(self, data):
        if data == "&nbsp;" or data == "\xa0":
            data = ""
        if self.data == READ_PROBLEM_NAME:
            self.problems.append(data)
        if self.data == READ_PLACE:
            if data == '':
                self.status = TOTAL
        if self.data == READ_TEAM:
            self.team = data
            self.teams.append(self.team)
            self.statuses[self.team] = [""] * len(self.problems)
        if self.data == READ_STATUS:
            if self.cur_attrs.get('data-dq'):
                self.statuses[self.team][self.problem] = 'DQ' + data
            else:
                self.statuses[self.team][self.problem] = data

        self.data = INACTIVE


def render_standings(group):
    cids = [x.contest_id for x in group.lessons.all() if x.contest_id > 0]
    parsers = []
    contests = []
    team_scores = {}
    for contest in cids:
        name = get_contest_name(contest)
        parser = Parser()
        parser.init()
        with open(get_path(contest), "r") as f:
            parser.feed(f.read())
        if parser.good:
            parsers.append(parser)
            if len(parsers) > 1:
                if set(parsers[-2].teams) != set(parsers[-1].teams):
                    return 'Rendering error'
            for team in parser.statuses:
                score = 0
                penalty = 0
                for q in parser.statuses[team]:
                    if q:
                        if q[0] == '+':
                            score += 1
                            penalty += int(q[1:] or "0")
                if team not in team_scores:
                    team_scores[team] = [0, 0]
                team_scores[team][0] += score
                team_scores[team][1] += penalty
            contests.append({"name": name, "problems": deepcopy(parser.problems), "table": deepcopy(parser.statuses)})
    scores = []
    for team in team_scores:
        scores.append(team_scores[team] + [team])
    scores.sort(key=lambda x: (-x[0], x[1], x[2]))
    prev = None
    places = {}
    for q in scores:
        cur = (q[0], q[1])
        if cur != prev:
            prev = cur
        if cur not in places:
            places[cur] = 1
        else:
            places[cur] += 1
    cur_place = 1
    prev = None
    prev_r = ""
    for q in scores:
        cur = (q[0], q[1])
        if cur == prev:
            r = prev_r
        else:
            r = str(cur_place)
            if places[cur] > 1:
                r += "-" + str(cur_place + places[cur] - 1)
            prev_r = r
        q += [r]
        cur_place += 1 
        prev = cur

    cnts_header = ""
    for contest in contests:
        cnts_header += """
                        <th class="st_prob" colspan="{problems}">{name}</th>""".format(name=contest['name'], problems=len(contest['problems']))

    prob_header = ""
    for contest in contests:
        for problem in contest['problems']:
            prob_header += """
                        <th class="st_prob">{name}</th>""".format(name=problem)

    body = ""
    for q in scores:
        body += """
                    <tr>
                        <td class="st_place">{place}</td>
                        <td class="st_team">{team}</td>
                        <td class="st_total">{total}</td>
                        <td class="st_pen">{pen}</td>""".format(place=q[3], team=q[2], total=q[0], pen=q[1])

        for contest in contests:
            row = contest['table'][q[2]]
            for run in row:
                cl = ""
                if run == "":
                    cl = "none"
                elif run[0] == "+":
                    cl = "ok"
                elif run[0] == "-":
                    cl = "fl"
                if run.startswith("DQ"):
                    cl = "dq"
                    run = run[2:]
                body += """
                        <td class="st_prob {cl}">{run}</td>""".format(cl=cl, run=run or "&nbsp;")
        body += """
                    </tr>"""
    
    return """<!doctype html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <link href="/ejudge/unpriv.css" type="text/css" rel="stylesheet" />
        <link href="/static/stand.css" type="text/css" rel="stylesheet" />
        <title>{group} - сводная таблица</title>
    </head>
    <body>
        <h1>{group} - сводная таблица</h1>
        <div class="table-wrapper">
            <table class="st">
                <thead>
                    <tr>
                        <th class="st_place" rowspan="2">Место</th>
                        <th class="st_team" rowspan="2">Участник</th>
                        <th class="st_total" rowspan="2">+</th>
                        <th class="st_pen" rowspan="2">Dirt</th>{cnts_header}
                    </tr>
                    <tr>{prob_header}
                    </tr>
                </thead>
                <tbody>{body}
                </tbody>
            </table>
        </div>
    </body>
</html>
""".format(group=group.short_name, cnts_header=cnts_header, prob_header=prob_header, body=body)
