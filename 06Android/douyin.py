#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : douyin.py
# @Time    : 2021/2/25 19:46
# @Author  : Merle
# @Site    : 
"""

"""
import time
import unittest

from appium import webdriver

desired_caps = {'platformName': 'Android',  # 平台名称
                'platformVersion': '7.1.2',  # 系统版本号
                'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                'appPackage': 'com.ss.android.ugc.aweme',  # apk的包名
                'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity'  # activity 名称
                }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
driver.implicitly_wait(8)
# 点击同意
time.sleep(3)
print('开始同意')
driver.find_element_by_id('com.ss.android.ugc.aweme:id/b9m').click()
# 向上滑动
window = driver.get_window_size()
x0 = window['width'] * 0.8  # 起始x坐标
x1 = window['width'] * 0.2  # 终止x坐标
y = window['height'] * 0.5  # y坐标
for i in range(4):
    driver.swipe(x0, y, x1, y, 500)
    time.sleep(1)

# window = self.driver.get_window_size()
# print(window)

# self.driver.find_element_by_accessibility_id('Mathbot Editor').click()
# btn_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.View/android.widget.GridView/android.widget.FrameLayout[{0}]/android.widget.FrameLayout'
# self.driver.find_element_by_xpath(btn_xpath.format(7)).click()
# self.driver.find_element_by_xpath(btn_xpath.format(10)).click()
# self.driver.find_element_by_xpath(btn_xpath.format(8)).click()
# time.sleep(3)

# 测试结束后执行的方法
# def tearDown(self):
#     self.driver.quit()
