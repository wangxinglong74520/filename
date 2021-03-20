#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 02shiping.py
# @Time    : 2021/1/31 13:42
# @Author  : Merle
# @Site    : 
"""
线程池元原则:线程池处理的是阻塞且耗时的操作
"""

import requests

from utils.header import get_ua
from utils.chaojiying import rec_code
import os
import json
from multiprocessing.dummy import Pool
from lxml import etree
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': get_ua()
}

url = 'https://www.pearvideo.com/category_5'
resp = requests.get(url, headers=headers).text
tree = etree.HTML(resp)
lis = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []
for li in lis:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]
    # 对详情页的url发起请求
    detail_page_next = requests.get(url=detail_url, headers=headers).text
    zi = etree.HTML(detail_page_next)
    ne = zi.xpath('//div[@id="poster"]/@data-cid')[0]
    url = 'https://www.pearvideo.com/videoStatus.jsp?contId={}&mrd=0.29042232579048459'.format(ne)
    data = {
        'contId': ne,
        'mrd': 0.29042232579048459
    }
    aj = requests.get(url=urls, headers=headers, params=data)

    dic = {
        'name': name,
        'url': aj  # 未解出
    }
    urls.append(dic)


# 对视频进行下载
def get_video_data(dic):
    url = dic['url']
    print(dic['name'], '正在下载...')
    data = requests.get(url=url, headers=headers).content
    with open(dic['name'], 'wb') as f:
        f.write(data)
        print(dic['name'], '下载完成')


# 使用进程池对视频进程请求
pool = Pool()
pool.map(get_video_data, urls)
