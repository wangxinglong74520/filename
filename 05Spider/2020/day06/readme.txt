爬虫第6天
一回顾上周知识点
1.1爬虫的认识
    数据请求
    数据解析(re/xpath/bs4)
    数据存储(csv/pmysql/json)
    反反爬的策略
        ip代理池
        ua池cookie池:收集手动登录之后的相应cookie信息
        请求间隔(2-5)
        验证码处理(打码平台.机器学习???)
1.2网络请求库
    urllib
        request
            urlopen()
            urlretrieve(fullurl,filename)
            Request(url,data=None,headers)
            build_opener(*handlers)
        parse
        quote()
        urlencode()

    requests(第三方)
        requests(method,url,params,data,json,files,headers,cookies,proxiesauth)
            get(url,params,**kwargs)
            post(url,data,json,**kwargs)
            put(url,data,json,**kwargs)
            delete(url,**kwargs)
            Response
                status_code
                encoding
                headers
                content 字节数据
                text 文本数据
                json()
1.3数据解析
    re
    xpath
        from lxml import etree
        root = etree.HTML(html)
        root.xpath('')
    bs4
        from bs4 import BeautifulSoup
        root = beautifulSoup(html,'lxml')
        查找元素
        find('标签名',class_,id_) 查找第一个
        find_all('标签名',class_,id_,limit=N)查找N个
        select('css选择器')
            id
            .classname
            标签名
            兄弟标签
            属性标签
            伪类
        Tag属性
            string/text
            get_text()
            attrs:dict标签中所有属性字典
            contents 子标签的文本列表
            descendants 子标签的Tag列表
1.4 多任务爬虫
    多线程
        threading
            Thread
        queue.Queue 线程队列
    多进程
        multiprocessing
            Process
            Queue 进程队列
    协程
        asyncio
            coroutine 协程装饰器
            get_event_loop()
            wait()
            sleep()
        yield from
        async/await
1.5selenium框架
- chrome.get() 打开目标(发起请求)
- chrome.quit() 退出浏览器
- chrome.close() 关闭当前的窗口
- chrome.find_element(By, value)
	- selenium.webdriver.common.by.By
		- ID
		- CLASS_NAME
		- NAME
		- XPATH
		- CSS_SELECTOR
		_ LINK_TEXT
	- WebElement 查到的标签对象
		- get_attribute('属性名', default)
		- text 标签文本
		- click()
		- send_keys()
		- rect 当前元素的位置(left, top, width, height)

- chrome.find_elements(By, value)
- execute_script()
- save_screenshot(filename)  截图
- 等待某一个标签元素出现
	- selenium.webdriver.support
		- ui
			- WebDriverWait
		- expected_conditions
			- visibility_of_all_elements_located((By, value))

	ui.WebDriverWait(dirver, timeout).until(
			expected_conditions,
			error_msg
	)
```
### 1.6 docker

```
容器技术，将远程的docker仓库中的镜像下拉到本地， 再将镜像运行成为一个容器(进程)。
```

```
- 镜像操作
	- 基本信息
		- 名称
		- 版本
		- ID
		- 描述
	- docker images 查看所有镜像
	- docker rmi 名称:版本号 / ID 删除镜像
	- docker run 名称:版本号 / ID 启动镜像
		- -dit 后台启动镜像，启动后可进入容器并打开新的terminal(终端)
		- -p 宿主机端口: 容器端口
- 容器操作
	- docker ps 查看正运行的容器
		- -a 查看所有的容器
		- -l 查看最后一个启动的容器

	- docker logs 容器名或ID  查看容器运行的日志
	- docker exec 容器名或ID Linux命令 在容器中执行Linux命令
		- docker exec -it 容器名或ID bash 进入容器
	- docker stop 容器名或ID
	- docker start 容器名或ID
	- docker restart 容器名或ID
	- docker rm -f 容器名或ID 删除容器， -f强制删除正运行的容器
```
三.scrapy
3.1 scrapy框架组成
五大核心
    engine 引擎 协调其他四个组件的联系,也是scrapy的核心框架
    spider 爬虫类
    scheduler 调度器 调度所有的请求
    downloader下载器,实现请求任务的执行
    itempipline数据管道,当spider解析完成后,将数据经engine转入到
二个中间件
爬虫中间件,介于spider和engine之间的,可以拦截spider的发起的请求及数据
下载中间件,介于engine和downloader之间的,可以拦截下载和响应

3.2应用框架
创建项目命令
    scrapy startproject 项目名称
创建爬虫命令
    scrapy genspider 爬虫名 域名
启动爬虫命令
    scrapy crawl 爬虫名
调试爬虫命令
    scrapy shell url
    scrapy shell
        fetch(url)
3.3Reponse类
    属性相关
        body响应的字节数据
        text 响应的编码之后文本数据
        headers响应头信息,是字节流数据
        encoding响应数据的编码字符集
        status 响应的状态码
        url 请求的url
        request 请求对象
        meta 元数据 用于request和callback回调函数之间传值
    解析相关
    selecor()
    css() 样式选择器--->返回selector选择器的可迭代(列表)对象
        scrapy.selector.SelectorList 选择器列表
        scrapy.selector.Selector
        样式选择器提取属性或文本
            ::text 提取文本
            ::attr("属性名") 提取属性

    xpath() xpath路径
        xpath路径,同lxml的xpath()相同
    选择器常用方法:
           css()/xpath()
           extract() 提取选择中的所有内容,返回的是list
           extract_first()/get()提取每个选择器中的内容,返回是文本
            lis.css('img').xpath('./@src').get()
            lis.css('img').x('./@src').get()
            lis.cs('img::attr("src")').get()















