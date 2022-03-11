#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ycnbc - CNBC data downloader
# https://github.com/asepscareer/ycnbc
#
# Copyright 2022 Asep Saputra
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

from lxml import html as _html
import requests as _requests
import pandas as _pd
from .utils import _BASE_URL_, _HEADERS_

def get_trendingnews():
    try:
        page = _requests.get(_BASE_URL_, headers=_HEADERS_)
        tree = _html.fromstring(page.content)
    except Exception:
        pass

    trending_news = tree.xpath("//li[contains(@class, 'TrendingNowItem')]")
    assert len(trending_news) > 0, 'Data Not Found'
    title, source = [], []

    for i in trending_news:
            text = i.xpath(".//a/text()")
            link = list(i.iterlinks())[0][2]

            title.append(' '.join(text))
            source.append(link)

    data = {
        'Title': title,
        'Link': source
    }
    df = _pd.DataFrame(data=data)
    return df

def get_latestnews():
    try:
        page = _requests.get(_BASE_URL_, headers=_HEADERS_)
        tree = _html.fromstring(page.content)
    except Exception:
        pass

    source, title, posttime = [], [], []

    links = tree.xpath("//a[contains(@class, 'LatestNews')]")
    assert len(links) > 0, 'Data Not Found'

    latest_news = tree.xpath("//ul[contains(@class, 'LatestNews')]")
    assert len(latest_news) > 0, 'Data Not Found'

    for i in links:
        source.append(list(i.iterlinks())[0][2])
    for i in latest_news:
        el = i.xpath("li")
        for rs in el:
            text = rs.xpath(".//a/text()")
            posttime_ = rs.xpath(".//span/time/text()")

            title.append(' '.join(text))
            posttime.append(' '.join(posttime_))

    data = {
        'Headline': title,
        'Post Time': posttime,
        'Link': source
    }
    df = _pd.DataFrame(data=data)
    return df
