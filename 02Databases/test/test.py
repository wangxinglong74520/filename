#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time     :2021-02-19  11:15
# @Author   :Merle
# @File     :test.py
"""     """
tuples = (('student',), ('teacher',), ('user',))
for tu in tuples:
    if 'user' in tu:
        print('True')
    else:
        print('False')