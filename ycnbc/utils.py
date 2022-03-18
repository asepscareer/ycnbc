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
from .uri import _BASE_URL_, _HEADERS_
from requests import get
from lxml import html
from pandas import DataFrame

def trending():
    try:
        page = get(_BASE_URL_, headers=_HEADERS_)
        tree = html.fromstring(page.content)
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
    df = build_df(data)
    return df


def latest():
    try:
        page = get(_BASE_URL_, headers=_HEADERS_)
        tree = html.fromstring(page.content)
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
    df = build_df(data)
    return df

def getnews(category):
    try:
        page = get("{}/{}".format(_BASE_URL_, category), headers=_HEADERS_)
        tree = html.fromstring(page.content)

        source, title, posttime = [], [], []
        news = tree.xpath("//div[contains(@class, 'Card-titleContainer')]")
        assert len(news)>0, 'Data Not Found'

        posttime_news = tree.xpath("//span[contains(@class, 'Card-time')]")
        assert len(posttime_news)>0, 'Data Not Found'

        for i in posttime_news:
            text = i.xpath(".//text()")
            posttime.append(' '.join(text))
        for i in news:
            text = i.xpath("..//div/text()")

            source.append(list(i.iterlinks())[0][2])
            title.append(' '.join(text))

        data = {
            'Headline': title,
            'Post Time': posttime,
            'Link': source
            }

        return build_df(data)
    except:
        msg = {
            'data': [None],
            'msg': ['This page or category contains news with PRO tags.']
            }
        return build_df(msg)

def build_df(values):
    df = DataFrame(data=values)
    df = df.convert_dtypes()
    return df