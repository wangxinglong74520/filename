#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : model.py
# @Time    : 2021/2/16 15:42
# @Author  : Merle
# @Site    : 
"""

"""


class User:
    def __init__(self, nameuser, password, phone=None):
        self.username = nameuser
        self.password = password
        self.phone = phone

    def __str__(self):
        return self.username
