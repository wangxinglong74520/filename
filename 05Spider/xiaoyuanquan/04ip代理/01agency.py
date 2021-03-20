#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01agency.py
# @Time    : 2021/1/28 22:37
# @Author  : Merle
# @Site    : 
"""

"""
import requests

from utils.header import get_ua
from utils.chaojiying import rec_code
import os
import json
from lxml import etree
# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context

# 创建session对象
headers = {
    'User-Agent': get_ua()
}

url = 'https://www.baidu.com/s?wd=ip'
proxies = {
    'https': '182.32.162.112:9999'
}
resp = requests.get(url=url, headers=headers,proxies=proxies)
with open('baidu.html', 'w', encoding='utf8') as f:
    f.write(resp.text)
