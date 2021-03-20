#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app6.py
# @Time    : 2021/2/15 15:16
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Flask, request, url_for, make_response, render_template

import setting

app = Flask(__name__)
app.config.from_object(setting)


class Girl:
    def __init__(self, name, adder):
        self.name = name
        self.adder = adder

    def __str__(self):
        return self.name


@app.route('/show')
def show():
    name = '小米'
    friends = ['xiaoming', '张三丰', '妲己', '兰陵王']
    dict1 = {'gift1': '大手', 'gift2': '鲜花'}
    # 创建对象
    girlfriend = Girl('美美', '上海')
    return render_template('show.html', name=friends, friends=friends,girl=girlfriend)


if __name__ == '__main__':
    app.run()
