#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time     :2021-01-25  17:52
# @Author   :Merle
# @File     :13ipagency.py
"""     """
import requests
from bs4 import BeautifulSoup
from lxml import etree
from utils.header import get_ua
import re
import os

headers = {
    'User-Agent': get_ua()
}

if __name__ == '__main__':
    url = 'https://www.89ip.cn/'
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    html = etree.HTML(resp.text)
    ips_list = html.xpath('//table[@class="layui-table"]/tbody/tr/td[1]/text()')
    ports_list = html.xpath('//table[@class="layui-table"]/tbody/tr/td[2]/text()')
    for ip, port in zip(ips_list, ports_list):
        proxy = ip.strip() + ':' + port.strip()
        print(proxy)

        proxiex = {
            # 'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy)
        }
