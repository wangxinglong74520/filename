#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app5.py
# @Time    : 2021/2/15 13:50
# @Author  : Merle
# @Site    : 
"""

"""
import json

from flask import Flask, request, render_template, redirect, url_for

import setting

app = Flask(__name__)
app.config.from_object(setting)
users = []


@app.route('/', endpoint='index')
def index():
    # 首页
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 注册
    if request.method == 'POST':  # 点击提交后使用post方法提交表单
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        user = {'username': username, 'password': password}
        users.append(user)
        # return '注册成功! <a href ="/">返回首页</a>'
        # return redirect('/')  # 有两次响应 1.302状态码 2.
        return redirect(url_for('index'))

    return render_template('register5.html')  # 使用get方法请求,进行表单填写


@app.route('/login')
def login():
    pass


@app.route('/show')
def show():
    # 所有注册信息
    # users list转为str
    j_str = json.dumps(users)
    return j_str


@app.route('/text')
def text():
    url = url_for('index')  # endpoint类似于小名  用于快速查找
    print(url)
    return 'text'


if __name__ == '__main__':
    app.run()
