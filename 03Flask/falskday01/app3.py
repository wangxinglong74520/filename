#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app3.py
# @Time    : 2021/2/14 14:08
# @Author  : Merle
# @Site    : 
"""
request
"""
from flask import Flask, request
import setting

app = Flask(__name__)
app.config.from_object(setting)


@app.route('/index')
def text():
    print(request.headers)
    print(request.path)
    print(request.url)
    print(request.full_path)
    return 'welcome '


if __name__ == '__main__':
    app.run()
