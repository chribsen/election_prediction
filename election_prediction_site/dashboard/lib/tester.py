from dashboard.models import Page, Party
from dashboard.lib.election_predictor import scraper
def test():
    scraper.Scraper().scrape()