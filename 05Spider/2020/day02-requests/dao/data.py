#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : data.py
# @Time    : 2020/11/25 22:15
# @Author  : Merle
# @Site    : 
# ******************       *************
import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='admin123',
    port=3306,
    charset='utf8'
)
cur = conn.cursor()
print(cur)

