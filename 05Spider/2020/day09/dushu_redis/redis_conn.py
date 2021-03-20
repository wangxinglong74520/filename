#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : redis_conn.py
# @Time    : 2021/2/22 21:22
# @Author  : Merle
# @Site    : 
"""

"""

import redis

client = redis.Redis(host='192.168.17.130', port=6378)
a = client.get('name')
print(a)
