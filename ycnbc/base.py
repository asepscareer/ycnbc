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

from .utils import getnews, latest, trending

class News():

    def latest(self):
        return latest()

    def trending(self):
        return trending()

    def economy(self):
        return getnews('economy')

    def jobs(self):  
        return getnews('jobs')

    def white_house(self):  
        return getnews('white-house')

    def hospitals(self):  
        return getnews('hospitals')

    def transportation(self):  
        return getnews('transportation')

    def jobs(self):  
        return getnews('jobs')

    def climate(self):  
        return getnews('climate')

    def media(self):  
        return getnews('media')

    def internet(self):  
        return getnews('internet')

    def congress(self):  
        return getnews('congress')

    def policy(self):  
        return getnews('policy')

    def finance(self):  
        return getnews('finance')

    def life(self):  
        return getnews('life')
    
    def defense(self):  
        return getnews('defense')
    
    def europe_politics(self):  
        return getnews('europe-politics')
    
    def china_politics(self):  
        return getnews('china-politics')
    
    def asia_politics(self):  
        return getnews('asia-politics')
    
    def world_politics(self):  
        return getnews('world-politics')
    
    def equity_opportunity(self):  
        return getnews('equity-opportunity')
    
    def politics(self):  
        return getnews('politics')

    def wealth(self):  
        return getnews('wealth')   

    def world_economy(self):  
        return getnews('world-economy')  

    def central_banks(self):  
        return getnews('central-banks')  

    def real_estate(self):  
        return getnews('real-estate')   

    def health_science(self):  
        return getnews('health-and-science')   

    def small_business(self):  
        return getnews('small-business')  

    def lifehealth_insurance(self):
        return getnews('life-and-health-insurance')

    def business(self):
        return getnews('business')
        
    def energy(self):
        return getnews('energy')

    def industrials(self):
        return getnews('industrials')

    def retail(self):
        return getnews('retail')
    
    def cybersecurity(self):
        return getnews('cybersecurity')
    
    def mobile(self):
        return getnews('mobile')

    def mobile(self):
        return getnews('technology')
    
    def cnbc_disruptors(self):
        return getnews('cnbc-disruptors')
    
    def tech_guide(self):
        return getnews('tech-guide')
    
    def social_media(self):
        return getnews('social-media')