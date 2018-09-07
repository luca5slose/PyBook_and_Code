import logging

LOG_FORMAT = "%(asctime)s--------%(levelname)s++++++%(message)s"
#format参数为
'''
asctime 	%(asctime)s 	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
  created 	%(created)f 	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
  relativeCreated 	%(relativeCreated)d 	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
  msecs 	%(msecs)d 	日志事件发生事件的毫秒部分
  levelname 	%(levelname)s 	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
  levelno 	%(levelno)s 	该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
  name 	%(name)s 	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
  message 	%(message)s 	日志记录的文本内容，通过 msg % args计算得到的
  pathname 	%(pathname)s 	调用日志记录函数的源码文件的全路径
  filename 	%(filename)s 	pathname的文件名部分，包含文件后缀
  module 	%(module)s 	filename的名称部分，不包含后缀
  lineno 	%(lineno)d 	调用日志记录函数的源代码所在的行号
  funcName 	%(funcName)s 	调用日志记录函数的函数名
  process 	%(process)d 	进程ID
  processName 	%(processName)s 	进程名称，Python 3.1新增
  thread 	%(thread)d 	线程ID
  threadName 	%(thread)s 	线程名称 
'''
logging.basicConfig(filename="test_log.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")





# 另外一种写法
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")