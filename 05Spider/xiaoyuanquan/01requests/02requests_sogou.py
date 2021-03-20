#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 02requests_sogou.py
# @Time    : 2021/1/24 14:43
# @Author  : Merle
# @Site    : 
"""

"""
import ssl
import requests
from fake_useragent import UserAgent

ssl._create_default_https_context = ssl._create_unverified_context

headers = {'user-agent': UserAgent().random}
print(headers)
if __name__ == '__main__':
    url = 'http://www.sogou.com/web'
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    response = requests.get(url, headers=headers, params=param)
    filename = kw + '.html'
    with open(f'case/{filename}', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print('保存成功')
