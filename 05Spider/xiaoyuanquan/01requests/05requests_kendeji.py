#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 05requests_kendeji.py
# @Time    : 2021/1/24 15:56
# @Author  : Merle
# @Site    : 
"""

"""
import requests
from utils.header import get_ua
import json
# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': get_ua()
}
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname':'',
        'pid':'',
        'keyword': '上海',
        'pageIndex': 1,
        'pageSize': 10,
    }
    resp = requests.post(url,data=data,headers=headers)
    if resp.status_code == 200:
        table = resp.json()
        print(len(table))