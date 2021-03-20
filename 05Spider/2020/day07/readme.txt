1.1日志模块
  import logging
  from logging import StreamHandler,fileHandler
    四个核心部分
        日志记录器logger:记录日志信息
        日志处理器handler:记录信息之后,由handler去处理
        日志过滤器filter:对记录信息进行过滤
        日志格式化formatter:由处理器对记录的信息按formatter格式进行处理(除HTTPHandler和SMTP之外)
    核心方法或者函数
        logging.getLogger(name) 默认没有name时,返回root
        logging.baseConfig() 配置root记录器的格式,处理器等.
        logging.info()/debug()/warning()/error()/critical() 由root记录器记录日志信息
    log

