#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : view.py
# @Time    : 2021/2/16 15:35
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Blueprint, request, render_template, redirect

from apps.user.model import User

user_bp = Blueprint('user', __name__)
# 列表保存的是一个一个的用户对象
users = []


@user_bp.route('/')
def user_center():
    return render_template('user/show.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # 获取提交数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg='用户名已经存在')
            # 创建用户
            user = User(username, password, phone)
            users.append(user)
            return redirect('/')
    return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return ''


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return ''


@user_bp.route('/del', methods=['GET', 'POST'])
def dell():
    # 删除
    # 获取你传递的username
    username = request.args.get('username')
    for user in users:
        # 删除用户名
        if user.username == username:
            users.remove(user)
            return '删除成功'
    else:
        return '删除失败'


@user_bp.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        realname = request.form.get('realname')
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        for user in users:
            if user.username == realname:
                user.username = username
                user.phone = phone
                return '更改成功'
    else:
        # get请求
        username = request.args.get('username')
        for user in users:
            if user.username == username:
                return render_template('user/update.html', user=user)
