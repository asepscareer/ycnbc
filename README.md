# Download news data from CNBC! CNBC's API

<table border=1 cellpadding=10><tr><td>

#### *** IMPORTANT LEGAL DISCLAIMER ***

---

ycnbc is **not** affiliated, endorsed, or vetted by CNBC, It's an open source tool that uses Web Scraping and is intended for research and educational purposes.
</td></tr></table>

---

**ycnbc** offers a threaded and Pythonic way to news and market data from [CNBC](https://www.cnbc.com).

[Changelog »](https://github.com/asepscareer/ycnbc/blob/master/CHANGELOG.rst)

---

## Why ycnbc is compelling:

- **Simplicity**: Easy-to-use API for quick data retrieval.
- **Directness**: No retries, ensuring immediate feedback on success or failure.
- **Focus**: Specifically designed for CNBC data, providing relevant and targeted information.
- **Lightweight**: Minimal dependencies for a streamlined experience.

---

## Quick Start

---
### Requirements

- Python >=3.8+
- curl-cffi>=0.5.9
- lxml>=4.5.1

---
### Installation

```
$ pip install ycnbc --upgrade --no-cache-dir
```

---

### Usage for Markets
```python
import ycnbc

markets = ycnbc.Markets()

quote_summary = markets.quote_summary('AAPL')
pre_markets = markets.pre_markets()
us_markets = markets.us_markets()
europe_markets = markets.europe_markets()
asia_markets = markets.asia_markets()
currencies = markets.currencies()
cryptocurrencies = markets.cryptocurrencies()
futures_and_commodities = markets.futures_and_commodities()
bonds = markets.bonds()
funds_and_etfs = markets.funds_and_etfs()
```

### Usage for news

```python
import ycnbc

news = ycnbc.News()

# Get trending news
trending_ = news.trending()

# Get latest news
latest_ = news.latest()

# Get news by category
economy_ = news.economy()
jobs_ = news.jobs()
white_house_ = news.white_house()
hospitals_ = news.hospitals()
transportation_ = news.transportation()
media_ = news.media()
internet_ = news.internet()
congress_ = news.congress()
policy_ = news.policy()
finance_ = news.finance()
life_ = news.life()
defense_ = news.defense()
europe_politics_ = news.europe_politics()
china_politics_ = news.china_politics()
asia_politics_ = news.asia_politics()
world_politics_ = news.world_politics()
equity_opportunity_ = news.equity_opportunity()
politics_ = news.politics()
wealth_ = news.wealth()
world_economy_ = news.world_economy()
central_banks_ = news.central_banks()
real_estate_ = news.real_estate()
health_science_ = news.health_science()
small_business_ = news.small_business()
lifehealth_insurance_ = news.lifehealth_insurance()
business_ = news.business()
energy_ = news.energy()
industrials_ = news.industrials()
retail_ = news.retail()
cybersecurity_ = news.cybersecurity()
mobile_ = news.mobile()
technology_ = news.technology()
cnbc_disruptors_ = news.cnbc_disruptors()
tech_guide_ = news.tech_guide()
social_media_ = news.social_media()
climate_ = news.climate()
```

Note:

- URL pages containing news content that have the `PRO` tag still cannot be retrieved using this library.

---

### Legal Stuff

**ycnbc** is distributed under the **Apache Software License**. See
the [LICENSE.txt](./LICENSE.txt) file in the release for details.

---

### P.S.

Please drop me a note with any feedback you have.

**Asep Saputra**