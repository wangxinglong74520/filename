#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 05_urllib_handlers.py
# @Time    : 2020/11/22 14:53
# @Author  : Merle
# @Site    : 
# ******************  多个urllib的请求处理器     *************
"""
多个urllib的请求处理器
"""
from urllib.request import build_opener, HTTPHandler, HTTPCookieProcessor, ProxyHandler, Request
from http.cookiejar import CookieJar
from urllib.parse import urlencode
opener = build_opener(HTTPHandler(),
                      HTTPCookieProcessor(CookieJar),
                      ProxyHandler(proxies={
                          'http': 'http://123.55.102.31:9999'
                      }))

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uriqueTimestamp=20182122180'

data = {
    'rkey': '1c7df63368df7ce73c234de26178ec11',
    'password': '19870115',
    'origURL': 'http://www.renren.com/home',
    'key_id': '1',
    'icode': '',
    'f': 'http://www.renren.com/224549540',
    'email': 'dqsygcz@126.com',
    'domain': 'renren.com',
    'captcha_type': 'web_login',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    ,'Referer':'http://www.renren.com/SysHome.do'
}

request = Request(post_url,
                  urlencode(data).encode('utf-8'),
                  headers)
resp = opener.open(request)  # http.client.HTTPResponse
bytes_ = resp.read()
print(bytes_.decode())
