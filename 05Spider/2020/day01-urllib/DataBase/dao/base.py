#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : base.py
# @Time    : 2020/11/22 17:00
# @Author  : Merle
# @Site    : 
# ******************       *************
from pymysql import Connection


class BaseDao:
    def __init__(self):
        self.conn = Connection()

    def query(self, table_name, *columns, where=None, whereargs=None):
        sql = 'select %s from %s'
        sql = sql % (','.join(columns), table_name)
        if where:
            sql += where
        with self.conn as c:
            if whereargs:
                c.execute(sql, whereargs)
            else:
                c.execute(sql)
            ret = c.fetchall() # list[<dict>,<dict>]
        return ret
    def save(self, table_name, instance):
        pass

    def update(self, table_name, instance, where, whereargs):
        pass

    def delete(self, table_name, where, whereargs):
        pass
