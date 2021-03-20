#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01josn.py
# @Time    : 2021/3/14 9:42
# @Author  : Merle
# @Site    : 
"""
eval() 可以将符合python语法的字符串直接执行
"""
import json
"""
python    json
True      true
False     false
字符串     字符串
字典       对象
列表，元祖   数组



"""
a = '1+1'
print(a)
print(eval(a))

person = {'name': 'zhangsan', 'age': 19}
s = '{"name": "zhangsan", "age": 19}'
m = json.dumps(person)  # dumps 将字典。列表，集合，元祖等转换为json字符串
print(type(m))

n = json.loads(s)  # loads 可以将json字符串转换为python里的数据
print(n)
