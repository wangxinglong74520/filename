#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01requests.py
# @Time    : 2021/1/24 14:15
# @Author  : Merle
# @Site    : 
"""
爬取搜狗首页
"""
import requests
from lxml import etree
from utils.header import get_ua
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': get_ua()
}
if __name__ == '__main__':
    url = 'https://news.163.com/'
    response = requests.get(url, headers=headers)
    response = etree.HTML(response.text)
    lis = response.xpath('//div[@class="ns_area list"]/ul/li')
    print(lis)
    # alist = [4, 5, 7, 8, 9]
    # for index in alist:
    #     # model_url = response.xpath(f'div[@class="ns_area list"]/ul/li[{index}]').xpath('./a/@href').extract_first()
    #     model_url = lis[index].xpath('./a/@href').get()
    #     print(model_url)
    #     print(index)
