import ycnbc
import unittest

categories = [
    'world-economy', 'central-banks', 'jobs',
    'economy', 'health-and-science', 'media',
    'climate', 'wealth', 'life',
    'small-business', 'finance',
    'transportation', 'real-estate', 'internet',
    'white-house', 'policy', 'congress',
    'hospitals', 'life-and-health-insurance'
    ]

class TestGetData(unittest.TestCase):
    def test_getTrendingnews(self):
        assert(ycnbc.get_trendingnews().empty is False)

    def test_getLatestnews(self):
        assert(ycnbc.get_latestnews().empty is False)

    def test_getDatanews(self):
        for i in categories:
            assert(ycnbc.get_datanews(i).empty is False)

if __name__ == '__main__':
    unittest.main()