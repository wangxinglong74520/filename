一.Python上下文
1.1什么是上下文
任意的python对象都可以使用上下文环境,使用with关键字,上下文是一个
代码片段的区域,当对象进入上下文环境时,解析器会调用对象的__enter__()
当对象退出上下文环境时,会调用对象的__exit__().
1.2为什么使用上下文
对象使用上下文环境时,为了确保对象正确的释放资源,避免出现内存遗漏.
存在以下对象会经常使用上下文with:
    文件操作对象open()
    数据库的连接conn
    线程锁Lock
1.3如何使用
1.3.1重写类的方法
上下文的两个核心方法
    class A:
        def __enter__(self):
            # 进入上下文时,被调用的
            # 必须 返回一个相关的对象
            print('--enter--')
            return  'disen'
        def __exit__(self,except_type,val,tb):
            # 退出上下文时,被调用
            # except_type 如果存在异常时,表示为异常类的实例对象
            # cal 异常的消息Message
            # tb 异常的跟踪栈
            print('---exit---')
            # 返回True 表示 存在的异常不向外抛出
            # 返回False 表示存在异常时,向外跑出
            return True

1.3.2 with中使用
with A() as ret:
    # ret 是对象
    print(ret)
    assert  isinstance(ret,str)
    print('ok')

二.Dao设计
DAO(Data Access Object)数据访问对象只是一种设计思想,目的是简化对
数据库层操作,针对实体类(数据模型类)对象,防装一套与数据库操作的SDK(Software Develope Kit)

合理的DAO的SDK的设计:
-dao(基础数据库操作模块)
  |-- __init__.py
  |-- base.py
-entity(实体类模块)
  |-- user
  |--order
-db(具体数据操作)
  |-- user_db.py
  |order_db.py
