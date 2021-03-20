# -*- coding: utf-8 -*-
import xlrd


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\文档\设备核对(90台).xlsx')
    # 获取所有sheet
    print(workbook.sheet_names())
    # #获取sheet
    sheet1_name = workbook.sheet_by_name('Sheet1')
    # # 根据sheet索引或者名称获取sheet内容
    # sheet2 = workbook.sheet_by_name('Sheet2')
    # # sheet的名称，行数，列数
    print(sheet1_name.nrows, sheet1_name.ncols)
    # 获取245列的内容
    cols2 = sheet1_name.col_values(1)
    cols4 = sheet1_name.col_values(3)
    cols5 = sheet1_name.col_values(4)
    print(len(cols5))
    # rows = sheet2.row_values(3) # 获取第四行内容
    # cols = sheet2.col_values(2) # 获取第三列内容
    # print rows
    # print cols
    # #获取单元格内容的三种方法
    print(sheet1_name.cell(1, 3).value)  # 行 列
    num = [1, 3, 4]  # 输入要求获取那一列的内容

    item = {}
    for x in range(1,int(sheet1_name.nrows)):  # 行数
        item['id'] = sheet1_name.cell(x, num[0])
        item["devices"] = sheet1_name.cell(x, num[1]).value
        item['name'] = sheet1_name.cell(x, num[2]).value
        print(item)
        return item




if __name__ == '__main__':
    read_excel()
