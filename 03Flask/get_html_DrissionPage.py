from DrissionPage import ChromiumPage
from DrissionPage._pages.session_page import SessionPage

"""
主页面对象有 3 种，它们通常是程序的入口：
    ChromiumPage：单纯用于操作浏览器的页面对象
    WebPage：整合浏览器控制和收发数据包于一体的页面对象
    SessionPage：单纯用于收发数据包的页面对象


@id	        #	    表示 id 属性，简化写法只在语句最前面且单独使用时生效
@class	    .	    表示 class 属性，简化写法只在语句最前面且单独使用时生效
text	    tx	    按文本匹配
@text()	    @tx()	按文本查找与 @ 或 @@ 配合使用时
tag	        t	    按标签类型匹配
xpath	    x	    用 xpath 方式查找元素
css	        c	    用 css selector 方式查找元素

# 查找tag为div的元素
ele = page.ele('tag:div')  # 原写法
ele = page('t:div')  # 简化写法
# 用xpath查找元素
ele = page.ele('xpath://xxxxx')  # 原写法
ele = page('x://xxxxx')  # 简化写法
# 查找text为'something'的元素
ele = page.ele('text=something')  # 原写法
ele = page('tx=something')  # 简化写法
"""
"""
page = WebPage()
# 登录邮箱
page.get("http://mail.163.com")
page('mail').clear()
page('mail').input("xxx") # 账户
page('#pwdtext').input("password") # 密码
page('#dologin').click() # 点击登录
# 等待加载
page.wait.load_start()
# 进入订阅邮件栏
page('xpath:/html/body/div[1]/nav/div[2]/ul/li[9]/div').click()
items = page('@class:tv0').eles('@class:nl0 hA0 ck0')
"""
# 定位元素、触发事件
# page = ChromiumPage()
page = SessionPage()
page.get('file:///D:/Codephone/BasicPlatform/report/task_2024_12_05_10_25_40/report.html')
ele2 = page.ele('xpath:.//table[@class="tests_by_suite"]//tr[@class="test_row"]')
ele3 = page('x:.//table[@class="tests_by_suite"]//tr[@class="test_row"]')
print(ele2)
print(ele3)
# items = page('x:.//table[@class="tests_by_suite"]').eles('x://tr[@class="test_row"]')
items = page.eles('x://tr[@class="test_row"]')
for item in items:
    # print("发件人："+item.ele('t:a').text, "主题："+item.ele('@class:da0').text)
    print(item.ele('x:/td[@class="col_name"]/a').text)
    # print("发件人：" + item.ele('t:a').text)
    print(item.ele('x:/td[@class="col_doc"]').text)
    # print(item.text)
