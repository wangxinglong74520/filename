#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : setting.py
# @Time    : 2021/2/17 11:54
# @Author  : Merle
# @Site    :
"""

"""


class Config:
    ENV = 'development'
    DEBUG = True
    # 配置mysql数据库
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flaskday05'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    # 开发环境
    ENV = 'development'


class ProductionConfig(Config):
    # 生产环境
    ENV = 'production'
    DEBUG = False
