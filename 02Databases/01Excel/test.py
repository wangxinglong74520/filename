# -*- coding: utf-8 -*-
import time

import xlrd
from pymysql import IntegrityError

from base import connect_mysql


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\文档\设备核对(90台)(1).xlsx')
    # 获取所有sheet
    # print(workbook.sheet_names())
    sheet1_name = workbook.sheet_by_name('Sheet1')
    # # 根据sheet索引或者名称获取sheet内容
    # # sheet的名称，行数，列数
    # print(sheet1_name.name,sheet1_name.nrows, sheet1_name.ncols)
    num = [1, 3, 4, 5, 6, 7, 8, 9]  # 输入要求获取那一列的内容
    data = []
    for x in range(1, int(sheet1_name.nrows)):  # 行数
        asset_id = sheet1_name.cell(x, num[0]).value
        device_number = sheet1_name.cell(x, num[1]).value
        name = sheet1_name.cell(x, num[2]).value
        region = sheet1_name.cell(x, num[3]).value
        status = sheet1_name.cell(x, num[4]).value
        borrow_id = sheet1_name.cell(x, num[5]).value
        device_belong = sheet1_name.cell(x, num[6]).value
        creator_id = sheet1_name.cell(x, num[7]).value
        creation_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        data.append(
            (creation_time, name, asset_id, device_number, region, int(status), int(borrow_id), device_belong,
             int(creator_id)))
    return data


def install_mysql(data):
    conn = connect_mysql('demo')
    # 创建游标
    cur = conn.cursor()
    # 查询数据库数据
    # aa = cur.execute('select * from phone_insert')
    # all_data = cur.fetchmany(aa)
    # asset_ids = []
    # for data in all_data:
    #     asset_ids.append(data[4])
    for id in data:
        print(id[2])
        if 'CN21090' in id[2] and len(id[2]) == 11:
            sql = 'insert into phone_insert(`creation_time`,`name`,`asset_id`,`device_number`,`region`,`status`,`borrow_id`,`device_belong`,`creator_id`) ' \
                  'values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            try:
                cur.execute(sql, id)
                conn.commit()
            except IntegrityError as e:
                print(e, f"插入资产编号重复：{id[2]}")
        else:
            print(f'字符串 {id[2]} 不符合条件')
    cur.close()
    conn.close()


if __name__ == '__main__':
    data = read_excel()
    install_mysql(data)
