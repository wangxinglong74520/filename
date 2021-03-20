#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : regex01.py
# @Time    : 2021/1/20 22:15
# @Author  : Merle
# @Site    : 
"""

"""

import re

msg = '娜扎热巴戴斯佟丽娅'
result = pattern = re.compile('佟丽娅')
# match() 从头开始搜索 搜索不到返回:None
pattern.match(msg)

s = '娜扎热巴戴斯佟丽娅'
result1 = re.match('佟丽娅',s)
print(result1)
#  search() 在整个字符串中查找
result2 = re.search('佟丽娅',s)
print(result2)
print(result2.span())  # 返回位置
print(result2.group())  # 返回匹配内容

msg = 'adbc7vikfd8hdf00'


"""
总结:
    . 任意字符
    ^ 开头
    & 结尾
    [] 范围 [abc] [a-z]  匹配[]内的内容
    正则预定义
    \s 空白
    \b 边界
    \d 数字
    \w word 字母 [0-9a-zA-Z_]
    
    大写反面 \S 非空格 \D非数字
    
    量词:
    * >=0
    + >=1
    ? 0,1
    手机号正则
    re.match(r'1[35789]\d{9}&',phone)
    {m} 固定m位
    {m,} >= m位
    {m,n} 在m到n位之间 
    () 表示一个整体
    [abc] 表示是一个字母
    
    分组:()  result.group() 获取组中的内容
    不需要引用的内容:
    
    需要引用的内容:
    1.number
    
    2.?P<名字>
    msg = '<html><h1>abc</h1></html>'
    result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
    
    re模块:
    match
    search
    findall
    sub(正则表达式,新内容,string) 找到的内容进行替换  新内容可以是个函数
    split() 切割 将切割的内容都保存打牌列表中
"""
result = re.sub(r'\d+','90','java:50,python:999')
print(result)

result = re.split(r'[,:]','java:50,python:999')
print(result)