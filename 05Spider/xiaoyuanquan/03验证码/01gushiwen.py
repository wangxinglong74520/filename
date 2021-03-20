#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01gushiwen.py
# @Time    : 2021/1/26 22:25
# @Author  : Merle
# @Site    : 

import requests

from utils.header import get_ua
from utils.chaojiying import rec_code
import os
import json
from lxml import etree
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 创建session对象
session = requests.Session()
headers = {
    'User-Agent': get_ua()
}
print(headers)
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
resp = requests.get(url, headers).text
root = etree.HTML(resp)
code = 'https://so.gushiwen.org' + root.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code, headers=headers).content
with open('code.jpg', 'wb') as f:
    f.write(img_data)
# 解析验证码
code = rec_code('code.jpg')
print(code)
post_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data = {
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '1544798456@qq.com',
    'pwd': 'admin123',
    'code': code,
    'denglu': '登录',
}
# 使用session进行post请求的发送
login = session.post(url=post_url, headers=headers, data=data)
print(login.status_code)

# 获取当前用户的个人页面数据
# 使用携带cookie的session进行get请求的发送
detail_url = 'https://so.gushiwen.org/user/collect.aspx'
detail_page_text = session.get(url=detail_url, headers=headers).text
