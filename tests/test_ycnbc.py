import ycnbc
import pytest


@pytest.fixture(scope='module')
def markets_instance():
    return ycnbc.Markets()


@pytest.fixture(scope='module')
def news_instance():
    return ycnbc.News()


def test_cnbc_news(news_instance):
    # List of categories to test
    categories = [
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
        'health-and-science',
        'small_business',
        'life_and_health_insurance',
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

    for category_name in categories:
        # Use getattr to dynamically call the method
        method = getattr(news_instance, category_name)
        response = method()
        assert isinstance(
            response, dict), f"Expected dict for {category_name}, got {type(response)}"
        assert "headline" in response and isinstance(
            response["headline"], list)
        assert "link" in response and isinstance(response["link"], list)
        if category_name == 'latest' or category_name == 'by_category':  # Only latest and by_category have 'time'
            assert "time" in response and isinstance(response["time"], list)
        assert len(
            response["headline"]) > 0, f"Expected non-empty headlines for {category_name}"


@pytest.mark.skip(reason="CNBC API is returning 403 Forbidden for market data, likely due to IP blocking or rate limiting.")
def test_cnbc_markets(markets_instance):
    quote_summary = markets_instance.quote_summary('AAPL')
    pre_markets = markets_instance.pre_markets()
    us_markets = markets_instance.us_markets()
    europe_markets = markets_instance.europe_markets()
    asia_markets = markets_instance.asia_markets()
    currencies = markets_instance.currencies()
    cryptocurrencies = markets_instance.cryptocurrencies()
    futures_and_commodities = markets_instance.futures_and_commodities()
    bonds = markets_instance.bonds()
    funds_and_etfs = markets_instance.funds_and_etfs()

    assert quote_summary is not None
    assert pre_markets is not None
    assert us_markets is not None
    assert europe_markets is not None
    assert asia_markets is not None
    assert currencies is not None
    assert cryptocurrencies is not None
    assert futures_and_commodities is not None
    assert bonds is not None
    assert funds_and_etfs is not None

    # Example of more specific assertions for market data
    assert isinstance(quote_summary, dict) and 'symbol' in quote_summary
    assert isinstance(pre_markets, list) and len(pre_markets) > 0
    # Add more specific assertions as needed for other market data types
