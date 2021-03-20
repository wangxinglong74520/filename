#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : view.py
# @Time    : 2021/2/17 11:57
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Blueprint, url_for,render_template

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def user_center():
    print()
    return '用户中心'


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

