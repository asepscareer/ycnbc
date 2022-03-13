import ycnbc
import unittest

categories = [
    'world-economy', 'us-economy', 'federal-reserve', 'central-banks', 'jobs', 'banks', 'investing',
    'hedge-funds', 'deals-and-ipos', 'insurance',
    'venture-capital', 'coronavirus', 'wall-street',
    'economy', 'health-and-science', 'media',
    'climate', 'wealth', 'life',
    'small-business', 'energy', 'finance',
    'transportation', 'industrials', 'real-estate',
    'retail', 'cybersecurity', 'enterprise',
    'internet', 'media', 'mobile',
    'white-house', 'china-politics', 'social-media',
    'policy', 'defense', 'congress',
    'hospitals', 'life-and-health-insurance'
    ]

class TestGetData(unittest.TestCase):
    def test_getTrendingnews(self):
        assert(ycnbc.get_trendingnews().empty is False)

    def test_getLatestnews(self):
        assert(ycnbc.get_latestnews().empty is False)

    def test_getDatanews(self):
        for i in categories:
            print(i)
            assert(ycnbc.get_datanews(i).empty is False)

if __name__ == '__main__':
    unittest.main()
