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

from .utils import CNBCNews


class News:
    def __init__(self):
        self.news = CNBCNews()

    def latest(self):
        return self.news.latest()

    def trending(self):
        return self.news.trending()

    def economy(self):
        return self.news.by_category('economy')

    def jobs(self):
        return self.news.by_category('jobs')

    def white_house(self):
        return self.news.by_category('white-house')

    def hospitals(self):
        return self.news.by_category('hospitals')

    def transportation(self):
        return self.news.by_category('transportation')

    def media(self):
        return self.news.by_category('media')

    def internet(self):
        return self.news.by_category('internet')

    def congress(self):
        return self.news.by_category('congress')

    def policy(self):
        return self.news.by_category('policy')

    def finance(self):
        return self.news.by_category('finance')

    def life(self):
        return self.news.by_category('life')

    def defense(self):
        return self.news.by_category('defense')

    def europe_politics(self):
        return self.news.by_category('europe-politics')

    def china_politics(self):
        return self.news.by_category('china-politics')

    def asia_politics(self):
        return self.news.by_category('asia-politics')

    def world_politics(self):
        return self.news.by_category('world-politics')

    def equity_opportunity(self):
        return self.news.by_category('equity-opportunity')

    def politics(self):
        return self.news.by_category('politics')

    def wealth(self):
        return self.news.by_category('wealth')

    def world_economy(self):
        return self.news.by_category('world-economy')

    def central_banks(self):
        return self.news.by_category('central-banks')

    def real_estate(self):
        return self.news.by_category('real-estate')

    def health_science(self):
        return self.news.by_category('health-and-science')

    def small_business(self):
        return self.news.by_category('small-business')

    def lifehealth_insurance(self):
        return self.news.by_category('life-and-health-insurance')

    def business(self):
        return self.news.by_category('business')

    def energy(self):
        return self.news.by_category('energy')

    def industrials(self):
        return self.news.by_category('industrials')

    def retail(self):
        return self.news.by_category('retail')

    def cybersecurity(self):
        return self.news.by_category('cybersecurity')

    def mobile(self):
        return self.news.by_category('mobile')

    def technology(self):
        return self.news.by_category('technology')

    def cnbc_disruptors(self):
        return self.news.by_category('cnbc-disruptors')

    def tech_guide(self):
        return self.news.by_category('tech-guide')

    def social_media(self):
        return self.news.by_category('social-media')

    def climate(self):
        return self.news.by_category('climate')
