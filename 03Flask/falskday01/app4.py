#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : app4.py
# @Time    : 2021/2/14 15:04
# @Author  : Merle
# @Site    : 
"""
app.py 与模板的结合使用
"""
from flask import Flask, request, render_template
import setting

app = Flask(__name__)
app.config.from_object(setting)


@app.route('/register')
def register():
    s = render_template('register.html')  # 将视图函数和模板结合
    return s


@app.route('/register2', methods=['GET', 'Post'])
def register2():
    print(request.full_path)
    print(request.path)
    # print(request.args)  # dict类型  get请求才能取到
    # print(request.args.get('username'))  #
    # print(request.args.get('password'))
    print(request.form)  # 如果请求方法是post则需要使用form取值
    return '进来了'


if __name__ == '__main__':
    print(app.url_map)
    app.run()
