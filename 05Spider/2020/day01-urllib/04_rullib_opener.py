#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 04_rullib_opener.py
# @Time    : 2020/11/22 12:59
# @Author  : Merle
# @Site    : 
# ******************   模仿浏览器增加不同的处理器    *************
# urllib.request.build_opener(*handlers)
# urllib.request.HTTPHandler  处理Http请求

from urllib.request import HTTPHandler, build_opener
import ssl
from collections import namedtuple

ssl._create_default_https_context = ssl._create_unverified_context
# 声明类  namedtuple(有命名的元祖类) 不可变的类
Response = namedtuple('Response',
                      field_names=['headers', 'code', 'text', 'body', 'encoding'])


def get(url):
    opener = build_opener(HTTPHandler())
    # 构建请求
    resp = opener.open(url)
    # 要求返回某一个类对象.他的属性包含:
    # headers-->dict,
    # code-->int,
    # text 文本,
    # body 字节码等相关属性
    headers = dict(resp.getheaders())
    try:
        encoding = headers['Content-Type'].split('=')[-1]
    except:
        encoding = 'utf-8'
    code = resp.code
    body = resp.read()
    text = body.decode(encoding)
    return Response(headers=headers, encoding=encoding, code=code,
                    body=body, text=text)


if __name__ == '__main__':
    resp: Response = get('http://jd.com')
    print(resp.code)
    # print(resp.text)
    print(resp.headers)
