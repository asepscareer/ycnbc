import ycnbc
import os
import json

markets = ycnbc.Markets()
news = ycnbc.News()

output_dir = "test_results"
os.makedirs(output_dir, exist_ok=True)

def save_output(category, data, prefix=""):
    filename = f"{prefix}{category.replace(' ', '_').replace('/', '_')}.json"
    filepath = os.path.join(output_dir, filename)
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Saved {category} data to {filepath}")
    except Exception as e:
        print(f"Error saving {category} data to {filepath}: {e}")

# MARKETS

try:
    quote_summary = markets.quote_summary('AAPL')
    save_output("quote_summary", quote_summary, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching quote_summary: {e}")

try:
    pre_markets = markets.pre_markets()
    save_output("pre_markets", pre_markets, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching pre_markets: {e}")

try:
    us_markets = markets.us_markets()
    save_output("us_markets", us_markets, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching us_markets: {e}")

try:
    europe_markets = markets.europe_markets()
    save_output("europe_markets", europe_markets, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching europe_markets: {e}")

try:
    asia_markets = markets.asia_markets()
    save_output("asia_markets", asia_markets, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching asia_markets: {e}")

try:
    currencies = markets.currencies()
    save_output("currencies", currencies, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching currencies: {e}")

try:
    cryptocurrencies = markets.cryptocurrencies()
    save_output("cryptocurrencies", cryptocurrencies, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching cryptocurrencies: {e}")

try:
    futures_and_commodities = markets.futures_and_commodities()
    save_output("futures_and_commodities", futures_and_commodities, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching futures_and_commodities: {e}")

try:
    bonds = markets.bonds()
    save_output("bonds", bonds, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching bonds: {e}")

try:
    funds_and_etfs = markets.funds_and_etfs()
    save_output("funds_and_etfs", funds_and_etfs, prefix="Markets - ")
except Exception as e:
    print(f"Error fetching funds_and_etfs: {e}")

# NEWS

try:
    trending_news = news.trending()
    save_output("trending", trending_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching trending news: {e}")

try:
    latest_news = news.latest()
    save_output("latest", latest_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching latest news: {e}")

try:
    economy_news = news.economy()
    save_output("economy", economy_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching economy news: {e}")

try:
    jobs_news = news.jobs()
    save_output("jobs", jobs_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching jobs news: {e}")

try:
    white_house_news = news.white_house()
    save_output("white_house", white_house_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching white_house news: {e}")

try:
    hospitals_news = news.hospitals()
    save_output("hospitals", hospitals_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching hospitals news: {e}")

try:
    transportation_news = news.transportation()
    save_output("transportation", transportation_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching transportation news: {e}")

try:
    media_news = news.media()
    save_output("media", media_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching media news: {e}")

try:
    internet_news = news.internet()
    save_output("internet", internet_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching internet news: {e}")

try:
    congress_news = news.congress()
    save_output("congress", congress_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching congress news: {e}")

try:
    policy_news = news.policy()
    save_output("policy", policy_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching policy news: {e}")

try:
    finance_news = news.finance()
    save_output("finance", finance_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching finance news: {e}")

try:
    life_news = news.life()
    save_output("life", life_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching life news: {e}")

try:
    defense_news = news.defense()
    save_output("defense", defense_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching defense news: {e}")

try:
    europe_politics_news = news.europe_politics()
    save_output("europe_politics", europe_politics_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching europe_politics news: {e}")

try:
    china_politics_news = news.china_politics()
    save_output("china_politics", china_politics_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching china_politics news: {e}")

try:
    asia_politics_news = news.asia_politics()
    save_output("asia_politics", asia_politics_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching asia_politics news: {e}")

try:
    world_politics_news = news.world_politics()
    save_output("world_politics", world_politics_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching world_politics news: {e}")

try:
    equity_opportunity_news = news.equity_opportunity()
    save_output("equity_opportunity", equity_opportunity_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching equity_opportunity news: {e}")

try:
    politics_news = news.politics()
    save_output("politics", politics_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching politics news: {e}")

try:
    wealth_news = news.wealth()
    save_output("wealth", wealth_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching wealth news: {e}")

try:
    world_economy_news = news.world_economy()
    save_output("world_economy", world_economy_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching world_economy news: {e}")

try:
    central_banks_news = news.central_banks()
    save_output("central_banks", central_banks_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching central_banks news: {e}")

try:
    real_estate_news = news.real_estate()
    save_output("real_estate", real_estate_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching real_estate news: {e}")

try:
    health_science_news = news.health_science()
    save_output("health_science", health_science_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching health_science news: {e}")

try:
    small_business_news = news.small_business()
    save_output("small_business", small_business_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching small_business news: {e}")

try:
    lifehealth_insurance_news = news.lifehealth_insurance()
    save_output("lifehealth_insurance", lifehealth_insurance_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching lifehealth_insurance news: {e}")

try:
    business_news = news.business()
    save_output("business", business_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching business news: {e}")

try:
    energy_news = news.energy()
    save_output("energy", energy_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching energy news: {e}")

try:
    industrials_news = news.industrials()
    save_output("industrials", industrials_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching industrials news: {e}")

try:
    retail_news = news.retail()
    save_output("retail", retail_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching retail news: {e}")

try:
    cybersecurity_news = news.cybersecurity()
    save_output("cybersecurity", cybersecurity_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching cybersecurity news: {e}")

try:
    mobile_news = news.mobile()
    save_output("mobile", mobile_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching mobile news: {e}")

try:
    technology_news = news.technology()
    save_output("technology", technology_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching technology news: {e}")

try:
    cnbc_disruptors_news = news.cnbc_disruptors()
    save_output("cnbc_disruptors", cnbc_disruptors_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching cnbc_disruptors news: {e}")

try:
    tech_guide_news = news.tech_guide()
    save_output("tech_guide", tech_guide_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching tech_guide news: {e}")

try:
    social_media_news = news.social_media()
    save_output("social_media", social_media_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching social_media news: {e}")

try:
    climate_news = news.climate()
    save_output("climate", climate_news, prefix="News - ")
except Exception as e:
    print(f"Error fetching climate news: {e}")
