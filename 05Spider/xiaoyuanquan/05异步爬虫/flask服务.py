#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : flask服务.py
# @Time    : 2021/1/31 15:31
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Flask
import time

app = Flask(__name__)


@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'Hello bobo'


@app.route('/jay')
def inde_jay():
    time.sleep()
    return 'Hello jay'


@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello tom'


if __name__ == '__main__':
    app.run(threaded=True)
