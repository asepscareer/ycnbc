import ycnbc
import unittest

data = ycnbc.News()


class TestData(unittest.TestCase):
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
                method = getattr(data, method_name)
                response = method()
                self.assertNotIn("error", response, f"{method_name} returned an error")


if __name__ == '__main__':
    unittest.main()
