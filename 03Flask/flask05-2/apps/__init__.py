#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2021/2/17 17:36
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Flask
from apps.user.view import user_bp
from ext import db
from setting import DevelopmentConfig


def create_app():
    app = Flask(__name__,template_folder='../templates')
    app.config.from_object(DevelopmentConfig)
    # 初始化db
    db.init_app(app=app)
    # 注册蓝图
    app.register_blueprint(user_bp)
    return app
