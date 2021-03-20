import xlrd
import time

from base import connect_mysql


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\文档\设备核对(90台)(1).xlsx')
    sheet1_name = workbook.sheet_by_name('Sheet1')
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
            (creation_time, name, asset_id, device_number, region, int(status), int(borrow_id), device_belong, int(creator_id)))
    # print(data)
    # install_data(data)
    return data


def install_data(data):
    for id in data:
        print(id[2])
        if 'CN21090' in id[2] and len(id[2]) == 11:
            with open('1.txt','a+',encoding='utf-8') as f:
                f.write(str(id)+'\n')
        else:
            print(f'字符串 {id[2]} 不符合条件')


if __name__ == '__main__':
    data = read_excel()
    install_data(data)
