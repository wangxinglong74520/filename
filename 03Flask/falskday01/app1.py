#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app1.py
# @Time    : 2021/2/13 21:54
# @Author  : Merle
# @Site    : 
"""
路由变量规则
"""
from flask import Flask
import setting

app = Flask(__name__)
app.config.from_object(setting)

data = {'a': '北京', 'b': '上海'}


@app.route('/')
def index():
    return '我是首页'


@app.route('/getcity/<key>')
def get_city(key):
    print(type(key))
    return data.get(key)


@app.route('/add/<int:num>')
def add(num):
    num = num + 10
    return str(num)


if __name__ == '__main__':
    app.run()
