#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : mongo_conn.py
# @Time    : 2021/2/22 22:03
# @Author  : Merle
# @Site    : 
"""

"""

from pymongo import MongoClient

client = MongoClient(host='192.168.17.130', port=27017)
client.auth('admin', '123456')
db = client.python201
# db.student.insert({'name':'tom','age':12})
print(db)
# for i in db.student.find():
#     print(i)