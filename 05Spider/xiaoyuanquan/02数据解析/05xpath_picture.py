#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 05xpath_picture.py
# @Time    : 2021/1/25 22:37
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
    filename = 'case/美女'
    if not os.path.exists(filename):
        os.makedirs(filename)
    for i in range(1,173):
        url = f'http://pic.netbian.com/4kmeinv/index_{i}.html'
        resp = requests.get(url,headers=headers)
        resp.encoding = 'gbk'
        tree = etree.HTML(resp.text)
        lis = tree.xpath('//ul[@class="clearfix"]/li')
        for li in lis:
            img = li.xpath('.//a/img/@src')[0]
            alt = li.xpath('.//a/img/@alt')[0]+'.jpg'
            # print(img,alt)
            img_url = 'http://pic.netbian.com'+img
            picture = requests.get(img_url,headers=headers).content
            img_path = filename+'/'+alt
            with open(img_path,'wb') as f:
                f.write(picture)
        print(f'正在下载,第{i}页图片')
        time.sleep(0.5)
























































