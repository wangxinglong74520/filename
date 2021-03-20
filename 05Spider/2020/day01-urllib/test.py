#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : test.py
# @Time    : 2020/11/21 15:01
# @Author  : Merle
# @Site    : 
# ******************       *************
import pymysql

def connectdb():
    print('连接到mysql服务器...')
    db = pymysql.connect(
        host="localhost",
        user="root",
        passwd="admin123",
        port=3306,
        db="stu",
        charset='utf8')
    print('连接上了!')
    return db
connectdb()