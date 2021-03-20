#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01_re.py
# @Time    : 2020/12/1 20:00
# @Author  : Merle
# @Site    : 
# ****************** 基于正则re解析数据      *************
import re
import os

import requests

from utils.header import get_ua
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
base_url = 'https://sc.chinaz.com/tupian/'
url = f'{base_url}shuaigetupian_3.html'
headers = {
    'User-Agent': get_ua()
}
if os.path.exists('mn.html'):
    with open('mn.html', encoding='utf-8') as f:
        html = f.read()
else:
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'  # 修改响应状态码
    # if resp.status_code == 200:
    #     print('请求成功')
    assert resp == 200
    html = resp.text
    with open('mn.html', 'w', encoding=resp.encoding) as f:
        f.write(html)
# print(html)
# 中文匹配:[\u4e00-\u9fa5]
compile2 = re.compile(r'<a target="(.*?)" href="(.*?)" alt="(.*?)">')
imgs2 = compile2.findall(html)  # 返回的是list
print(len(imgs2), imgs2, sep='\n')
# 获取下一页的
next_url = re.findall(r'<b>25</b></a><a href="(.*?)" class="nextpage">',html,re.S)
print(base_url+next_url[0])
