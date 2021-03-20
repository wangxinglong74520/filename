#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : models.py
# @Time    : 2021/2/17 17:47
# @Author  : Merle
# @Site    : 
"""

"""
from datetime import datetime

from ext import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username= db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(12),nullable=False)
    phone = db.Column(db.String(11),unique=True)
    rdatetime = db.Column(db.DateTime,default=datetime.now())

    def __str__(self):
        return self.username
