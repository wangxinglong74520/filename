#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01_request.py
# @Time    : 2020/11/22 18:32
# @Author  : Merle
# @Site    : 
# ******************       *************
# 上海二手房
import requests
from requests import Response

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://shanghai.anjuke.com/community/'

# 变量名后缀,类型,好处是编程时会自动提醒对象中的属性方法
resp: Response = requests.get(url, params={'from': 'navigation'})
print(resp.status_code)
print(resp.headers['content-type'])
print(resp.cookies)


# 声明函数时,参数名后面的`:类型`表示参数值的类型
# 在函数的()后`->类型`表示函数返回的数据(结果)类型
def download(url: str) -> str:
    # resp: Response = requests.get(url, params={'from': 'navigation'})
    resp: Response = requests.request('get', url, params={'from': 'navigation'})
    if resp.status_code == 200:
        return resp.text  # 文本 resp.content 字节码
    return '下载失败'


def get_douban_json():
    # 请求方法是post
    url = 'https://movie.douban.com/j/chart/top_list'
    data = {
        'start': 1,
        'limit': 20,
        'type': 5,
        'interval_id': '100:90',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    resp = requests.post(url, data=data, headers=headers)
    assert resp.status_code == 200
    if 'application/json' in resp.headers['content-type']:
        return resp.json()
    return resp.text


douban = get_douban_json()
print(douban)
