from django.test import TestCase
from election_prediction_site.dashboard.lib.election_predictor import scraper

class ScraperTestCase(TestCase):

    def test_scrape(self):
        """Animals that can speak are correctly identified"""
        print('hello')
        #scraper_obj = scraper.Scraper()
        #scraper_obj.scrape()