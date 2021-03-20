requests库
2.1安装环境
    pip install requests -i https://mirrors.alyun.com/pypi/simple
2.2核心函数
    requests.request() 所有方法的基本方法
        以下是request()方法参数说明
        method:str  请求指定方法 GET,POST,PUT,DELETE
        url:str  请求的资源接口(API),在RESTful规范中即是URL(统一资源标识符)
        params:dict 用于GET请求的查询参数
        data:dict 用于POST/PUT/DELETE请求的表单参数(Form Data)
        json:dict 用于上传json参数,封装到body(请求体)中,请求
        头的Content-Type默认为application/json
        files:dict 结构{'name':file-like-object|tuple}
        auth:授权
        如果是tuple则有三种情况:
            ('filename',file-like-object)
            ('filename',file-like-object,content_type)
            ('filename'file-like-object,content_type,custom-headers)
          指定files用于上传文件,一般使用post请求,默认请求头的content-Type
          为multipart/form-data类型.
          headers/cookies:dict
          proxies:dict,设置代理
          auth:tuple 用于授权的用户名和口令,形式('username'.'pwd')
    requests.get()  发起get请求 查询数据
      可用参数:
        url
        params
        json
        headers/cookies/auth
    requests.post()  发起post请求 上传/添加数据
      可用参数
        url
        data
        json
        files
        headers/cookies/auth
    requests.out()   发起PUT请求,修改或者更新数据
    requests.patch HTTP幂等性的问题,可以出现重复提交,不建议提交
    requests.delete() 发起delete请求 删除数据
    requests.session() --->session对象,可以调用
    s.get()/post()/put()/delete()等方法,多次请求的会话
2.3 requests.Response
以上的请求方法返回的对象类型是Response,对象常用的属性如下:
    status_code 响应状态码
    url  请求的url
    headers:dict 响应的头,相对于urllib的响应对象的getheaders(),但不包含cookies.
    cookies: 可迭代的对象,元素是Cookie类的对象(name,value,path)
    text: 响应的文本信息
    content:响应的字节数据
    encoding:响应数据的编码字符集,如utf-8,gbk,gb2312
    json():如果响应数据类型为application/json,则将响应的数据进行反序列化成
    python的list或者dict对象.
        扩展-javascript的序列化和反序列化
        JSON.stringify(obj)序列化
        JSON.parse(text)反序列化
