from django.core.management.base import BaseCommand, CommandError
from dashboard.lib.election_predictor import scraper


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        print str(parser)

    def handle(self, *args, **options):
        scraper.Scraper().scrape()