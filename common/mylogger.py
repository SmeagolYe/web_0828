import logging
from logging.handlers import RotatingFileHandler
from common.dir_config import *
import time

# 日志生成的时间、日志级别、文件名、函数名、调用logging的代码行
fmt = "%(asctime)s %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ]"

#工作日缩写名称、十进制表示的月份、缩写月份名称、年、时、分、秒
# datefmt的格式是设置%(asctime)s的显示格式
# Thu, 20 Aug 2020 17:24:18 ERROR base_page.py wait_element [ line:21 ]
datefmt = "%a, %d %b %Y %H:%M:%S"

handler1 = logging.StreamHandler()
curTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

handler2 = RotatingFileHandler(logs_dir + "/Web_AutoTest_{0}.log".format(curTime), backupCount=1)

logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler1, handler2])