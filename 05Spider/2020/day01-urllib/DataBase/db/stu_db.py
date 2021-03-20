#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : stu_db.py
# @Time    : 2020/11/22 17:12
# @Author  : Merle
# @Site    : 
# ******************       *************

from dao.base import BaseDao
from entity import Student


class StuDao(BaseDao):
    def query(self, where=None, args=None):
        return super(StuDao, self).query('Student', 'sn', 'name', 'sex', where=where, whereargs=whereargs)


if __name__ == '__main__':
    dao = StuDao()
    print(dao.query())
