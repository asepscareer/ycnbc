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
- pandas>=0.24.0
- requests>=2.26
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

# get trending news
trending_ = ycnbc.get_trendingnews() # return DataFrame

# get latest news
latest_ = ycnbc.get_latestnews() # return DataFrame

# get data by categories or urls
data_ = ycnbc.get_datanews('economy') # return DataFrame
```
or,
```
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
for i in categories:
    print(ycnbc.get_datanews(i))
```
**note** -> The category parameter is a URL.
For example, if you want to retrieve data from the url https://www.cnbc.com/economy/, then you can simply call it `ycnbc.get_datanews('economy')`.
---

### Legal Stuff

**ycnbc** is distributed under the **Apache Software License**. See
the [LICENSE.txt](./LICENSE.txt) file in the release for details.

---

### P.S.

Please drop me an note with any feedback you have.

**Asep Saputra**
