#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2020/11/22 16:44
# @Author  : Merle
# @Site    : 
# ******************   实体类对象  *************

class Student:
    def __init__(self,sn,name,age,sex):
        self.sn = sn
        self.name = name
        self.age =age
        self.sex = sex

    def __str__(self):
        return '%s->%s' % (self.sn,self.name)