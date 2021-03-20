#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app8.py
# @Time    : 2021/2/15 16:48
# @Author  : Merle
# @Site    : 
"""
            过滤器
"""
from flask import Flask, request, url_for, make_response, render_template

import setting

app = Flask(__name__)
app.config.from_object(setting)


@app.route('/show1')
def show1():
    girls = ['杨幂', '如花', '孙艺珍', '孙尚香', '貂蝉', '林允儿']
    users = [
        {'user': '战三1', 'passwd': 123121},
        {'user': '战三2', 'passwd': 2112123},
        {'user': '战三3', 'passwd': 3121233},
    ]
    msg = '<h1>520快乐</h1>'
    n1 = 'hello'
    return render_template('show-8.html', girls=girls, users=users, msg=msg,
                           n1=n1)


if __name__ == '__main__':
    app.run()
