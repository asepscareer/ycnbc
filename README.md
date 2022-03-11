# Download news data from CNBC! CNBC's API

<table border=1 cellpadding=10><tr><td>

#### \*\*\* IMPORTANT LEGAL DISCLAIMER \*\*\*

---

ycnbc is **not** affiliated, endorsed, or vetted by CNBC, It's
an open-source tool that uses Yahoo's publicly available APIs, and is
intended for research and educational purposes.
</td></tr></table>

---

**ycnbc** offers a threaded and Pythonic way to news and market data from [CNBC](https://www.cnbc.com).

[Changelog »](https://github.com/asepscareer/ycnbc/blob/main/CHANGELOG.rst)

---

## Quick Start

---
### Requirements

Python >=3.5+
pandas>=0.24.0
requests>=2.26
lxml>=4.5.1

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
trending_ = ycnbc.get_trendingnews()

# get latest news
latest_ = ycnbc.get_latestnews()
```
---

### Legal Stuff

**ycnbc** is distributed under the **Apache Software License**. See
the [LICENSE.txt](./LICENSE.txt) file in the release for details.

---

### P.S.

Please drop me an note with any feedback you have.

**Asep Saputra**
