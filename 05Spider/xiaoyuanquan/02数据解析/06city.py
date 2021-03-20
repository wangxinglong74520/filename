#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 06city.py
# @Time    : 2021/1/25 23:30
# @Author  : Merle
# @Site    : 
"""

"""
import re
import time

import requests
from utils.header import get_ua
import os
import json
from lxml import etree

# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': get_ua()
}


if __name__ == '__main__':
    # url = 'https://www.aqistudy.cn/historydata/'
    # resp = requests.get(url,headers).text
    # root = etree.HTML(resp)
    # host_city = root.xpath('//div[@class="top"]/div[@class="bottom"]/ul/li')
    # # 获取热门城市名称
    # all_city_name = []
    # for li in host_city:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_name.append(city_name)
    # # 获取全部城市名称
    # all_city_names = []
    # all_city = root.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li')
    # for ul in all_city:
    #     city = ul.xpath('./a/text()')
    #     all_city_names.append(city)
    url = 'https://www.aqistudy.cn/historydata/'
    resp = requests.get(url, headers).text
    root = etree.HTML(resp)
    a_list = root.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(len(all_city_names),all_city_names)