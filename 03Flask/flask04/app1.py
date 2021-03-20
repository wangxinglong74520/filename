#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app1.py
# @Time    : 2021/2/16 13:09
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Flask, render_template
import setting

app = Flask(__name__)
app.config.from_object(setting)


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/macro')
def user_macro():
    return render_template('macro1.html')


if __name__ == '__main__':
    app.run()
