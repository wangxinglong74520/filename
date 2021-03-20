#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time     :2021-02-19  11:00
# @Author   :Merle
# @File     :create_table.py
"""     """
from pymysql import IntegrityError

from base import connect_mysql

conn = connect_mysql('test')
# 创建游标
cur = conn.cursor()
# execute执行sql语句
cur.execute('show tables')
# 创建表
data_name = 'user'
# fetchall 获取所有数据
all_tables = cur.fetchall()
print(all_tables)
list_table = []
for tables in all_tables:
    print(tables)
    list_table.append(tables[0])
print(list_table)
# 判断表是否存在
if not data_name in list_table:
    cur.execute(
        f'create table {data_name}(`id` int primary key auto_increment,`name` varchar(32),`password` varchar(32),`age` int,`tel` varchar(150) unique)charset=utf8')
    print(f'{data_name}表创建成功！！')
else:
    print('表已经存在')

# 删除表
# cur.execute(f'drop table {data_name}')
# 插入数据
sqli = f'insert into {data_name}(name,age,tel) values(%s,%s,%s)'
try:
    cur.executemany(sqli, [
        ('Tom', '6', 13049145091),
        ('Jack', '7', '13049145015'),
        ('jerry', '7', '13049145195')
    ])
    conn.commit()  # 提交数据
except IntegrityError as e:
    print(e, "插入电话号码重复")
print('数据插入成功！！！')
cur.close()
conn.close()
