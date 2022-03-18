import ycnbc
import unittest

data = ycnbc.News()
class TestData(unittest.TestCase):
    def test_trending(self):
        assert(data.trending().empty is False)
        assert(data.latest().empty is False)
        assert(data.economy().empty is False)
        assert(data.health_science().empty is False)
        assert(data.finance().empty is False)
    

if __name__ == '__main__':
    unittest.main()