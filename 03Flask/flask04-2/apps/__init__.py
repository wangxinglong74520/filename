#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2021/2/16 15:21
# @Author  : Merle
# @Site    : 
"""

"""
from flask import Flask
from apps.user.view import user_bp

import setting


def create_app():
    app = Flask(__name__)  # app 是一个核心对象
    app.config.from_object(setting)  # 加载设置
    # 蓝图
    app.register_blueprint(user_bp)
    print(app.url_map)

    return app
