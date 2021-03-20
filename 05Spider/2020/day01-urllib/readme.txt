一.什么是爬虫
1.1爬虫Spider的概念
  爬虫用于爬取数据,又称为数据采集程序.
  爬取的数据来源于,网络中的数据可以是由Web服务器(Nginx/Apache),数据库服务器(MySql,Redis),
索引库(ElastichSearch),大数据(Hbase/Hive),视频/图片库,云存储
  爬取的数据是公开的,非盈利的.
1.2Python爬虫
  使用Python编写的爬虫脚本可以完成定时,定量,指定目标
  (Web站点)的数据爬取,主要使用多(单)线程/进程,网络请求库,
  数据解析,数据存储,任务调度等技术.
Python爬虫工程师,可以完成接口测试,功能测试,性能测试和集成测试.

二.爬虫与Web后端服务器之间的关系
爬虫使用网络请求库,相当于客户端请求,Web后端服务请求响应数据.
爬虫即向Web服务器发起HTTP请求,正确地接收响应数据,然后根据数据的类型进行数据的解析及存储.
爬虫程序在发起请求前,需要伪造浏览器(User-Agent指定请求头),
然后再向服务器发起请求,响应200的成功率高很多.

三.Python爬虫技术的相关库
网络请求:
    urllib对应python3  --->python2 对应Urllib2
    request
    selenium(UI自动测试,动态js渲染)
    appium(手机App的爬虫或UI测试)
数据解析:
    re正则
    xpath
    bs4
    json  序列化(把对象序列化成字符串或者字节)和反序列化(字符串或者字节转成对象)
数据存储
    pymysql
    mongodb
    elasticsearch
多任务库:
    多线程(threading),线程队列queue
    协程(asynio,gevent/eventlet)
爬虫框架
    scrapy
    scrapy-radis 分布式(多机爬虫)

四.常见反爬虫的策略
  UA(User-Agent)反扒策略
  登录限制(Cookie)
  请求频次(IP代理)
  验证码(图片-云打码,文字或者物件图片选择,滑块)
  动态js(selenium/Splash/api接口)

五.爬虫库urllib
    urllib.request 模块
        urlopen(url | request:Request,data=None) data是bytes类型
        urlretrieve(url,filename) 下载url的资源到指定的文件
        build_opener(*handlder)构建浏览器对象
             opener.open(url|request,data=None) 发起请求
        Request 构建请求的类
        HTTPHandler HTTP协议请求处理器
            ProxyHandler(proxies={'http':'http://proxy_ip:port'}) 代理处理---- 限制请求
        HTTPCookieProcessor(CookieJar())
    urllib.parse模块
        quote(txt) 将中文字符串转成url编码
        urlencode(query:dict)将参数的字典转成url编码,结果是
        key=value&key=value形式


处理器:Handle
  1.定制更高级的处理请求
  2.步骤
       1.创建handle对象: handler = urllib.request.HTTPHandler()
       2.创建opener对象: opener = urllib.request.build_opener(handler)
       3.创建Request对象:
       4.发送Request请求:opener.open(req)


















