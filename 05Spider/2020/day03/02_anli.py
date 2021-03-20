#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 02_anli.py
# @Time    : 2020/12/2 23:52
# @Author  : Merle
# @Site    : 
# ******************       *************

from lxml import etree
import urllib.request
import urllib.parse
import os

url = 'http://sc.chinaz.com/tupian/shuaigetupian.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

# 获取请求到的html字符串
html_string = response.read().decode('utf-8')

# 将html字符串转换成etree结构
html_tree = etree.HTML(html_string)

# 解析名字和图片
src_list = html_tree.xpath('//div[@id="container"]//div[starts-with(@class,"box")]/div/a/img/@src2')
src_name = html_tree.xpath('//div[@id="container"]//div[starts-with(@class,"box")]/div/a/img/@alt')

# 下载到本地
for index in range(len(src_list)):
    pic_url = src_list[index]
    suffix = os.path.splitext(pic_url)[-1]
    file_name = 'images/' + src_name[index] + suffix

    urllib.request.urlretrieve(pic_url, file_name)
