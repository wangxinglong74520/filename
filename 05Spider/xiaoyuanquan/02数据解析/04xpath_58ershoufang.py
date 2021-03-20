#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 04xpath_58ershoufang.py
# @Time    : 2021/1/25 21:47
# @Author  : Merle
# @Site    : 
"""
爬取58二手房
"""
import re
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
# print(headers)
if __name__ == '__main__':
    url = 'https://sh.58.com/ershoufang/'
    page_text = requests.get(url,headers=headers).text
    tree = etree.HTML(page_text)
    divs = tree.xpath('//section[@class="list"]/div')
    pf = open('../case/58二手房.text', 'w', encoding='utf-8')
    for div in divs:
        title = div.xpath('.//div[@class="property-content-title"]/h3/@title')
        address = div.xpath('.//p[@class="property-content-info-comm-address"]//text()')
        price = div.xpath('.//p[@class="property-price-total"]//text()')
        print(title,address,price)
        pf.write(str(title+address+price))










