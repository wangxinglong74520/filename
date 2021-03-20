#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 03requests_baidu.py
# @Time    : 2021/1/24 15:11
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
    url = 'https://fanyi.baidu.com/sug'
    data ={
        'kw':'dog'
    }
    response = requests.post(url,headers=headers,data=data)
    dic_obj = response.json()
    fanayi = dic_obj['data']
    print(dic_obj)
    print(fanayi[0]['v'])

    fp = open('case/dog.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over')