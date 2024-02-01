import os
import re
import xlrd
import xlwt
import openpyxl


def rend_excel():
    file_path = '1.xlsx'
    wb = xlrd.open_workbook(file_path)
    sheet_names = wb.sheet_names()
    ws = wb.sheet_by_name(sheet_names[0])
    # 获取所有的行
    nrows = ws.nrows
    # 获取所有的列
    result = []
    ncols = ws.ncols
    # 通过循环获取到表格中所有用例，id和名称
    type_lists = ['','','','','','']
    type_li = []
    for i in range(nrows):
        case_type = ws.cell_value(i, 0)
        if case_type in type_lists and case_type != '':
            type_li.append((case_type, i))
    # print(type_li)
    type_name = {}
    for i in range(len(type_li) - 1):
        for j in range(type_li[i][1], type_li[i + 1][1]):
            case_id = ws.cell_value(j, 2)
            case_name = ws.cell_value(j, 3)
            case_level = ws.cell_value(j, 4)
            if case_id != '':
                type_name.setdefault(type_li[i][0], []).append((case_id, case_name, case_level))
    return type_name


def module_classify():
    """
    获取适配完成的用例
    :return:
    """
    type_name = rend_excel()
    file_path = r'case_nopass.xlsx'
    wb = xlrd.open_workbook(file_path)
    sheels = wb.sheet_names()
    ws = wb.sheet_by_name(sheels[-1])
    print(sheels[-1])
    nrows = ws.nrows
    print(nrows, '-------case_nopass----总共适配数量----')
    num = 0
    n = 0
    type_name_data = {}
    cz = []
    for i in range(1, nrows):
        cass_id = ws.cell_value(i, 0)
        if cass_id != '':
            n += 1
            for i, y in type_name.items():
                for x in y:
                    if cass_id == x[0]:
                        cz.append(cass_id)
                        x = list(x)
                        # type_name_data.setdefault(str(i).split(' ')[-1], []).append(x)
                        type_name_data.setdefault(i, []).append(x)
                        num += 1
    if os.path.exists('1.txt'):
        os.remove('1.txt')
    for i in range(1, nrows):
        cass_id = ws.cell_value(i, 0)
        if cass_id != '' and cass_id not in cz:
            with open('1.txt', 'a', encoding='utf-8') as f:
                f.write('{}\n'.format(cass_id))

    print('1：', num)
    print('1：', n)
    print('1：', nrows - 1)
    print('*' * 30)
    return type_name_data


def move_file_Application(file_path):
    """
    1
    :param file_path: 1
    :return:
    """
    # 所有用例集
    type_name = rend_excel()
    # 适配完成用例集
    cases = module_classify()
    now_files = []
    zong_num = 0
    for root, dirname, filenames in os.walk(file_path):
        if dirname != '' and filenames != '':
            for filename in filenames:
                if filename.endswith('.py'):
                    now_files.append((filename[:-3], os.path.join(root, filename)))
                    zong_num += 1
    print('1：', zong_num)
    # 筛选本地适配用例
    num = 0
    is_no_num = 0
    filepath = {}
    is_yes = []
    # 本地所有存在适配用例
    is_no = []
    is_nono = []
    if os.path.exists('1.txt'):
        os.remove('1.txt')
    for mod, case in cases.items():
        for ca in case:
            for file in now_files:
                # if ca[0] == file[0]:
                is_yes.append(ca[0])
                filepath.setdefault(mod, []).append((ca[0], ca[1], ca[2], '已适配'))
                num += 1
    for mod, case in cases.items():
        for ca in case:
            if ca[0] not in is_yes:
                with open('1.txt', 'a', encoding='utf-8') as f:
                    f.write('{}\n'.format(ca[0]))

    for case in now_files:
        if case[0] not in is_yes:
            is_no.append(case[0])

    # 筛选本地未适配用例
    # 本地存在的用例
    is_case = []
    is_case_num = 0
    for file in is_no:
        for mod, case in type_name.items():
            for ca in case:
                if file == ca[0]:
                    is_case.append(file)
                    filepath.setdefault(mod, []).append((ca[0], ca[1], ca[2], '未适配'))
                    is_case_num += 1

    # 筛选本地存在线上不存在用例
    is_case_no = []
    is_case_no_num = 0
    for file in is_no:
        if file not in is_case:
            is_case_no.append(file)
    for file in is_case_no:
        for mod, case in type_name.items():
            for ca in case:
                if file == ca[0]:
                    filepath.setdefault(mod, []).append((ca[0], ca[1], ca[2], '不存在用例'))
                    is_case_no_num += 1
    filetxt = '02.txt'
    if os.path.exists(filetxt):
        os.remove(filetxt)
    for i in is_case_no:
        with open(filetxt, 'a', encoding='utf-8') as f:
            f.write((i + ';' + '\n'))
    # print('不存在',is_case_no)
    # print(len(is_no), '-----------is_no------------')
    # print(num, '----------------', is_no_num)
    # print('总共用例：{},存在用例：{}条'.format(zong_num, num))
    # print('不存在用例：{}'.format(zong_num - num))
    # file_path = file_path.split("\\")[-1]
    # filetxt = '{}不存在用例.txt'.format(file_path)
    # if os.path.exists(filetxt):
    #     os.remove(filetxt)
    # for i in Applica:
    #     with open(filetxt, 'a', encoding='utf-8') as f:
    #         f.write((i + ';' + '\n'))
    nnn = 0

    for x, y in filepath.items():
        for k in y:
            nnn += 1
    print(nnn, '---------------')
    print('：', num, len(is_yes))
    print('：', is_case_no_num + is_case_num + num)
    print('', len(is_case_no))
    return filepath


def write_excel_module_classify(file_path):
    type_name_data = move_file_Application(file_path)
    csv_file = '.xls'
    if os.path.exists(csv_file):
        os.remove(csv_file)
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('Sheet1', cell_overwrite_ok=True)
    # 设置字体
    style = xlwt.XFStyle()
    # 字体
    font = xlwt.Font()
    font.name = '微软雅黑'
    font.height = 20 * 12
    style.font = font
    # 边框
    border = xlwt.Borders()
    border.top = 1
    border.bottom = 1
    border.left = 1
    border.right = 1
    style.borders = border
    # 对齐方式
    alignment1 = xlwt.Alignment()
    alignment1.vert = 0x01
    alignment1.horz = 0x01
    style.alignment = alignment1

    # 设置格式2
    style2 = xlwt.XFStyle()
    # 字体
    font = xlwt.Font()
    font.name = '微软雅黑'
    font.height = 20 * 12
    style2.font = font
    # 边框
    border = xlwt.Borders()
    border.top = 1
    border.bottom = 1
    border.left = 1
    border.right = 1
    style2.borders = border
    # 对齐方式
    alignment1 = xlwt.Alignment()
    alignment1.vert = 0x01
    alignment1.horz = 0x02
    style2.alignment = alignment1

    # 设置格式2
    style3 = xlwt.XFStyle()
    # 字体
    font = xlwt.Font()
    font.name = '微软雅黑'
    font.height = 20 * 12
    style3.font = font
    # 边框
    border = xlwt.Borders()
    border.top = 1
    border.bottom = 1
    border.left = 1
    border.right = 1
    style3.borders = border
    # 对齐方式
    alignment1 = xlwt.Alignment()
    alignment1.vert = 0x01
    alignment1.horz = 0x02
    style3.alignment = alignment1
    # 设置背景颜色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 3
    style3.pattern = pattern

    # 设置格式4
    style4 = xlwt.XFStyle()
    # 字体
    font = xlwt.Font()
    font.name = '微软雅黑'
    font.height = 20 * 12
    style4.font = font
    # 边框
    border = xlwt.Borders()
    border.top = 1
    border.bottom = 1
    border.left = 1
    border.right = 1
    style4.borders = border
    # 对齐方式
    alignment1 = xlwt.Alignment()
    alignment1.vert = 0x01
    alignment1.horz = 0x02
    style4.alignment = alignment1
    # 设置背景颜色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 2
    style4.pattern = pattern
    # 获取的用例字典去重
    module_name_deduplicate = {}
    module_name_deduplicate_list = []
    for n, m in type_name_data.items():
        for d in m:
            if d not in module_name_deduplicate_list:
                module_name_deduplicate_list.append(d)
                module_name_deduplicate.setdefault(n, []).append(d)

    num_pass = 0
    num_fail = 0
    lie_list = []
    module_names = module_name_deduplicate.keys()
    for i in module_names:
        nm = len(module_name_deduplicate.get(i))
        lie_list.append(nm)
    # print(len(lie_list), '-------------------')
    # print(lie_list)
    n = 1
    h = 0
    # 将所有发现的问题写道一起
    for i, y in module_name_deduplicate.items():
        """
        合并单元格使用ws.merge_cells()方法，参数介绍：
        start_row: 开始合并的行。
        start_column: 开始合并的行。
        end_row: 结束合并的列。
        end_column: 结束合并的列。这四个值所在的行/列都会被合并（闭区间）。"""
        # sheet.write(n, 0, i, style2)
        sheet.write_merge(n, n + lie_list[h] - 1, 0, 0, i, style2)
        # print(n, n + lie_list[h] - 1, 0, 0, i)
        sheet.write(0, 0, '', style)
        sheet.write(0, 1, '', style)
        sheet.write(0, 2, '', style)
        sheet.write(0, 3, '', style2)
        sheet.write(0, 4, '', style2)
        # print(y)
        for x in y:
            sheet.write(n, 1, x[0], style)
            # write_merge合并单元格
            # sheet.write_merge(n, n, 1, 2, x[0], style)
            sheet.write(n, 2, x[1], style)
            # sheet.write_merge(n, n, 3, 4, x[1], style)
            sheet.write(n, 3, x[2], style2)
            style_cl = style
            if x[3] == '已适配':
                num_pass += 1
                style_cl = style3
            elif x[3] == '未适配':
                num_fail += 1
                style_cl = style4
            sheet.write(n, 4, x[3], style_cl)
            n += 1
        h += 1
    print('本次写入用例数：', n)
    wb.save(csv_file)


if __name__ == '__main__':
    """
  
    """
    # rend_excel()
    # compare_excel()
    # write_excel()
    # module_classify()
    write_excel_module_classify(r'')
    try:
        pass
    except Exception as e:
        print(e)
