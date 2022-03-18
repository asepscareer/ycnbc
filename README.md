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

# get trending news
trending_ = data.trending() # return DataFrame

# get latest news
latest_ = data.latest() # return DataFrame

# get news by category
economy_ = data.economy() # return DataFrame

# etc.
```

Note:

- URL pages containing news content that have the `PRO` tag still cannot be retrieved using this library.

---

### Legal Stuff

**ycnbc** is distributed under the **Apache Software License**. See
the [LICENSE.txt](./LICENSE.txt) file in the release for details.

---

### P.S.

Please drop me an note with any feedback you have.

**Asep Saputra**
