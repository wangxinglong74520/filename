#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 0612306.py
# @Time    : 2021/1/31 19:46
# @Author  : Merle
# @Site    : 
"""
12306火车票
"""
from utils.header import get_ua
from utils.chaojiying import rec_code
from selenium import webdriver
from time import sleep
from PIL import Image
from selenium.webdriver import ActionChains

chrome = webdriver.Chrome()

chrome.get('https://kyfw.12306.cn/otn/resources/login.html')
chrome.maximize_window()
sleep(1)
chrome.find_element_by_css_selector('.login-hd-account').click()
# 截图
chrome.save_screenshot('./aa.png')
#  截取验证码图片区域
# 获取验证码位置坐标
code_img_ele = chrome.find_element_by_id('J-loginImg')
location = code_img_ele.location  # 验证码图片左上角的坐标x,y
print(location)
size = code_img_ele.size  # 宽度
print('size', size)
# 左上角和右下角坐标
rangle = (
    location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']
)
# 图片截取
i = Image.open('aa.png')
frame = i.crop(rangle)
frame.save('12306.png')
# 验证码图片解析
sleep(2)
code = rec_code('12306.png')
print(code)
# 通过验证码坐标点击验证码
all_list = []
if '|' in code:
    list_1 = code.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = list_1[i].split(',')[0]
        y = list_1[i].split(',')[1]
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = code.split(',')[0]
    y = code.split(',')[1]
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
sleep(2)
# 遍历列表,使用动作链对每一个列表元素对应的x,y指定的位置进行操作
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(chrome).move_to_element_with_offset(code_img_ele, int(x), int(y)).click().perform()
    sleep(0.5)
# 输入用户名密码,点击登录
chrome.find_element_by_id('J-userName').send_keys('17693173557')
chrome.find_element_by_id('J-password').send_keys('5201314wxl')
sleep(3)
# 点击登录
chrome.find_element_by_id('J-login').click()

# 动作链
action = ActionChains(chrome)
# 点击长按指定的标签
hua = chrome.find_element_by_id('nc_1__bg')
action.click_and_hold(hua)
# move_by_offset(x,y) x向水平方向拖动,y竖直    perform()立即执行动作链操作
action.move_by_offset(300, 0).perform()
# 释放动作链
action.release()
