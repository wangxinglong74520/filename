#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app7.py
# @Time    : 2021/2/15 15:50
# @Author  : Merle
# @Site    : 
"""

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
    return render_template('show-7.html', girls=girls,users=users)


if __name__ == '__main__':
    app.run()
