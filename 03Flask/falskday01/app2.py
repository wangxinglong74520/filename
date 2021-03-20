#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app2.py
# @Time    : 2021/2/14 12:44
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Flask, Response
import setting

app = Flask(__name__)
app.config.from_object(setting)


@app.route('/index')
def text():
    return '北京'
# return 后面返回的字符串其实也是做了一个response对象的封装,最终结果还是response对象


@app.route('/text')
def text():
    return {'a': '北京', 'b': '上海'}


@app.route('response')
def response():
    return Response('大家中午吃什么')


if __name__ == '__main__':
    app.run()
