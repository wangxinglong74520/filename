#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : models.py
# @Time    : 2021/2/17 16:03
# @Author  : Merle
# @Site    : 
"""

"""
# ORM 类 ---> 表
# 类对象 --> 表中的一条记录
from datetime import datetime

from ext import db


class User(db.Model):
    # db.Column() 映射表中的列
    """
    类型:
        db.Integer  int
        db.String(11)  varchar(11)

    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    rdatetime = db.Column(db.DateTime, default=datetime.now())

    def __str__(self):
        return self.username


# class UserInfo(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     realname = db.Column(db.String(20))
#     gender = db.Column(db.Boolean, default=False)
#
#     def __str__(self):
#         return self.realname
