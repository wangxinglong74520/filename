三 动态js渲染
3.1 Selenium
3.2 Splash
    Splash 是web服务,基于webkit技术框架,可以动态加载网页

一.回顾知识点
1.1协程的爬虫
协程和线程的区别:
    线程是CPU调度的,多线程是共享同一进程中的内存的(线程本地变量local,同步lock,条件变量)
    线程-->threading模块
    协程是在线程(主线程)中声明以及调度的,协程是由程序调度的,是基于事假模型
    (IO多路复用模型-select/poll/epoll)
    协程--->asyncio模块
    协程的知识点:
        @asyncio.coroutine将函数升级为协程对象(闭包函数实现)
        yield from 将执行的权限交给其他协程对象
        loop = asyncio.get_event_loop() 获取事件模型对象
        loop.run_until_complete(协程对象)事件模型启动协程,直到协程执行完成后,释放模型对象.
            如果是多个协程对象时,需要使用asyncio.wait()将多个协程对象以元祖的方式传入wait()方法中.

        Python 3.5+增加两个关键字
        async 代替@asyncio.coroutine
        await 代替yield from
        注意:async和await必须同时使用的

1.2 selenium库
    安装
    下载浏览器驱动
    在python中使用
        selenium.webdriver.common.bu.BY
            BY.CLASS_NAME
            BY.CSS_SELECTOR
            BY.ID
            BY.NAME
            BY.TAG_NAME
            BY.XPATH
            BY.LINK_TEXT 连接的地址
        selenium.webdriver.Chrome
            在实例化Chrome()对象中需要指定浏览器驱动
            chrome.get(url) 打开url
            chrome.find_element(by,value)根据by查找value的一个元素
            chrome.window_handlers:list 可以获取窗口标签页
            chrome.execute_script(js) 当前窗口中执行js脚本
            chrome.swich_to.window/frame() 切换窗口
            chrome.save_screenshot('a.png') 截屏
            chrome.get_cookies() 获取当前网页的cookie
            chrome.get_screenshot_as_file(filename) 当前网页保存为文件
            chrome.get_window_rect()  窗口的位置 left/right/bottom
            chrome.get_window_size() width height
            chrome.get_window_position()
        WebElement 是查找元素的对象类型
        from selenium.webdriver.remote.webelement import WebElement
            click() 点击
            send_keys() 输入内容
        等待WebElement元素的出现
            selenium.webdriver.support 模块
                ui
                    WebDriverWait(driver,timeout)
                        until(expected_conditions,msg)
                expected_conditions
                        visibility_off_all_elements_located(By,value) 在当前窗口都可见的value


四.自动化测试
python单元测试模块-unittest.TestSuit









