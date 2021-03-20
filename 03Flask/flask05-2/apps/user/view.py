#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : view.py
# @Time    : 2021/2/17 17:47
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Blueprint, request, render_template

from apps.user.models import User
from ext import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            # 与模型结合
            # 1.找到模型类并创建对象
            user = User()
            # 2. 给对象赋值
            user.username = username
            user.password = password
            user.phone = phone
            # 添加到数据库
            # 3.将user对象添加到session中(类似缓存)
            db.session.add(user)
            # 4.提交数据部分
            db.session.commit()
            return '用户添加成功'
        else:
            return '两次密码不一致'
    return render_template('user/register.html')
