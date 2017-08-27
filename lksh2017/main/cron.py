from main.models import Group
from main.standings import render_standings
from lksh.settings import STANDINGS_DIR
import os.path

def update_standings():
    for group in Group.objects.all():
        path = os.path.join(STANDINGS_DIR, 'group_%d.html' % group.id)
        with open(path, 'w') as f:
            f.write(render_standings(group))
