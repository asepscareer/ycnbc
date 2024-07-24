# Download news data from CNBC! CNBC's API

<table border=1 cellpadding=10><tr><td>

#### \*\*\* IMPORTANT LEGAL DISCLAIMER \*\*\*

---

ycnbc is **not** affiliated, endorsed, or vetted by CNBC, It's an open source tool that uses Web Scraping and is intended for research and educational purposes.
</td></tr></table>

---

**ycnbc** offers a threaded and Pythonic way to news and market data from [CNBC](https://www.cnbc.com).

[Changelog »](https://github.com/asepscareer/ycnbc/blob/master/CHANGELOG.rst)

---

## Quick Start

---
### Requirements

- Python >=3.5+
- requests>=2.23.0
- lxml>=4.5.1

---
### Installation

```
$ pip install ycnbc --upgrade --no-cache-dir
```

---

### Usage

```python
import ycnbc

data = ycnbc.News()

# Get trending news
trending_ = data.trending()

# Get latest news
latest_ = data.latest()

# Get news by category
economy_ = data.economy()
jobs_ = data.jobs()
white_house_ = data.white_house()
hospitals_ = data.hospitals()
transportation_ = data.transportation()
media_ = data.media()
internet_ = data.internet()
congress_ = data.congress()
policy_ = data.policy()
finance_ = data.finance()
life_ = data.life()
defense_ = data.defense()
europe_politics_ = data.europe_politics()
china_politics_ = data.china_politics()
asia_politics_ = data.asia_politics()
world_politics_ = data.world_politics()
equity_opportunity_ = data.equity_opportunity()
politics_ = data.politics()
wealth_ = data.wealth()
world_economy_ = data.world_economy()
central_banks_ = data.central_banks()
real_estate_ = data.real_estate()
health_science_ = data.health_science()
small_business_ = data.small_business()
lifehealth_insurance_ = data.lifehealth_insurance()
business_ = data.business()
energy_ = data.energy()
industrials_ = data.industrials()
retail_ = data.retail()
cybersecurity_ = data.cybersecurity()
mobile_ = data.mobile()
technology_ = data.technology()
cnbc_disruptors_ = data.cnbc_disruptors()
tech_guide_ = data.tech_guide()
social_media_ = data.social_media()
climate_ = data.climate()
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
