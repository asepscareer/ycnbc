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
from lxml import html
from requests import get
from .uri import _BASE_URL_, _HEADERS_


class CNBCNews:
    def __init__(self):
        self.base_url = _BASE_URL_
        self.headers = _HEADERS_

    def _fetch_page(self, endpoint=""):
        """
        Fetches and parses the web page content.

        Args:
            endpoint (str): The specific endpoint to fetch data from.

        Returns:
            html.Element: Parsed HTML tree if successful, otherwise an error dictionary.
        """
        try:
            url = f"{self.base_url}/{endpoint}" if endpoint else self.base_url
            page = get(url, headers=self.headers)
            page.raise_for_status()  # Ensure we raise an error for bad HTTP responses
            return html.fromstring(page.content)
        except Exception as e:
            return {"error": str(e)}

    def trending(self):
        """
        Fetches trending news.

        Returns:
            dict: Dictionary containing titles and links of trending news, or an error message.
        """
        try:
            tree = self._fetch_page()
            if "error" in tree:
                return tree

            trending_news = tree.xpath("//li[contains(@class, 'TrendingNowItem')]")
            if not trending_news:
                return {"error": "Data Not Found"}

            title, source = [], []
            for i in trending_news:
                text = i.xpath(".//a/text()")
                link = list(i.iterlinks())[0][2] if list(i.iterlinks()) else None
                title.append(' '.join(text))
                source.append(link)

            return {
                'Title': title,
                'Link': source
            }
        except Exception as e:
            return {"error": str(e)}

    def latest(self):
        """
        Fetches the latest news.

        Returns:
            dict: Dictionary containing headlines, post times, and links of the latest news, or an error message.
        """
        try:
            tree = self._fetch_page()
            if "error" in tree:
                return tree

            source, title, posttime = [], [], []

            links = tree.xpath("//a[contains(@class, 'LatestNews')]")
            if not links:
                return {"error": "No Latest News links found"}

            latest_news = tree.xpath("//ul[contains(@class, 'LatestNews')]")
            if not latest_news:
                return {"error": "No Latest News list found"}

            for i in links:
                link = list(i.iterlinks())[0][2] if list(i.iterlinks()) else None
                source.append(link)

            for i in latest_news:
                el = i.xpath("li")
                for rs in el:
                    text = rs.xpath(".//a/text()")
                    posttime_ = rs.xpath(".//span/time/text()")

                    title.append(' '.join(text))
                    posttime.append(' '.join(posttime_))

            return {
                'Headline': title,
                'Post Time': posttime,
                'Link': source
            }
        except Exception as e:
            return {"error": str(e)}

    def by_category(self, category):
        """
        Fetches news based on the category.

        Args:
            category (str): The news category to fetch.

        Returns: dict: Dictionary containing headlines, post times, and links for the specified category, or an error
        message.
        """
        try:
            tree = self._fetch_page(category)
            if "error" in tree:
                return tree

            source, title, posttime = [], [], []

            news = tree.xpath("//div[contains(@class, 'Card-titleContainer')]")
            if not news:
                return {"error": "No news items found"}

            posttime_news = tree.xpath("//span[contains(@class, 'Card-time')]")
            if not posttime_news:
                return {"error": "No post time found"}

            for i in posttime_news:
                text = i.xpath(".//text()")
                posttime.append(' '.join(text))

            for i in news:
                text = i.xpath("..//div/text()")
                link = list(i.iterlinks())[0][2] if list(i.iterlinks()) else None
                source.append(link)
                title.append(' '.join(text))

            return {
                'Headline': title,
                'Post Time': posttime,
                'Link': source
            }
        except Exception as e:
            return {"error": str(e)}
