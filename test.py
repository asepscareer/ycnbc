import ycnbc

class Test():
    def test_trendings():
        assert(ycnbc.get_trendingnews().empty is False)

    def get_latestnews():
        assert(ycnbc.get_latestnews().empty is False)