#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2021/2/17 11:50
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Flask

import setting
from apps.user.view import user_bp
from ext import db


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(setting.DevelopmentConfig)

    db.init_app(app)  # 将db对象对象与app进行关联
    # 注册蓝图
    app.register_blueprint(user_bp)

    return app
