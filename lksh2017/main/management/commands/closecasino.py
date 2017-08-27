from django.core.management.base import BaseCommand, CommandError
from main.casino import close_casino

class Command(BaseCommand):
    help = 'Closes all casino sessions, rewards players and renders results'

    def handle(self, *args, **options):
        close_casino()
