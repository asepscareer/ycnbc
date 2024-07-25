import ycnbc
import unittest
import json


class TestData(unittest.TestCase):

    def setUp(self):
        self.markets = ycnbc.Markets()
        self.news = ycnbc.News()

    def test_cnbc_news(self):
        methods = [
            'latest',
            'trending',
            'economy',
            'jobs',
            'white_house',
            'hospitals',
            'transportation',
            'media',
            'internet',
            'congress',
            'policy',
            'finance',
            'life',
            'defense',
            'europe_politics',
            'china_politics',
            'asia_politics',
            'world_politics',
            'equity_opportunity',
            'politics',
            'wealth',
            'world_economy',
            'central_banks',
            'real_estate',
            'health_science',
            'small_business',
            'lifehealth_insurance',
            'business',
            'energy',
            'industrials',
            'retail',
            'cybersecurity',
            'mobile',
            'technology',
            'cnbc_disruptors',
            'tech_guide',
            'social_media',
            'climate'
        ]

        for method_name in methods:
            with self.subTest(method=method_name):
                method = getattr(self.news, method_name)
                response = method()
                self.assertNotIn("error", response, f"{method_name} returned an error")

    def test_cnbc_markets(self):
        quote_summary = self.markets.quote_summary('AAPL')
        pre_markets = self.markets.pre_markets()
        us_markets = self.markets.us_markets()
        europe_markets = self.markets.europe_markets()
        asia_markets = self.markets.asia_markets()
        currencies = self.markets.currencies()
        cryptocurrencies = self.markets.cryptocurrencies()
        futures_and_commodities = self.markets.futures_and_commodities()
        bonds = self.markets.bonds()
        funds_and_etfs = self.markets.funds_and_etfs()

        print(json.dumps(funds_and_etfs))
        self.assertIsNotNone(quote_summary)
        self.assertIsNotNone(pre_markets)
        self.assertIsNotNone(us_markets)
        self.assertIsNotNone(europe_markets)
        self.assertIsNotNone(asia_markets)
        self.assertIsNotNone(currencies)
        self.assertIsNotNone(cryptocurrencies)
        self.assertIsNotNone(futures_and_commodities)
        self.assertIsNotNone(bonds)
        self.assertIsNotNone(funds_and_etfs)


if __name__ == '__main__':
    unittest.main()
