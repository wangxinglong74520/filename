#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : regex02.py
# @Time    : 2021/1/21 21:52
# @Author  : Merle
# @Site    : 
"""
分组
"""
import re

# 匹配数字0-100数字
n = '100'
result = re.match(r'[1-9]?/d?$|100$', n)
print(result)

# 验证邮箱  163 126 qq
email = '1544798456@qq.com'
result = re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)$', email)
print(result)

msg = '<html><h1>abc</h1></html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
print(result.group(1))
print(result.group(2))
print(result.group(3))

# 不是以4,7结尾的手机号码
phone = '17693331255'
result = re.match(r'1\d{9}[0-35-689]$', phone)
print(result)

# 爬虫
phone = '010-12345678'
result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
print(result)
# 分别提取
# () 表示分组 group(1) 表示提取的第一组
print(result.group(1))
print(result.group(2))

msg = '<html>abc</html>'
msgl = '<hl>hello</hl>'
result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$',msg)
print(result.group(1))

# number  \1 引用第一组
result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$',msg)
print(result)

msg = '<html><h1>abc</h1></html>'
result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
print(result.group(1))
print(result.group(2))
print(result.group(3))

# 非贪念








