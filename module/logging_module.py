# __author: ioi
# date: 2021/6/3
# 日志
import logging

# filemode默认是a
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S', filename='log.log', filemode='w')
logging.debug('1')
logging.info('2')
logging.error('3')
logging.critical('4')

logger = logging.getLogger()
# 设置日志级别
logger.setLevel(logging.DEBUG)
# 控制台输出
ch = logging.StreamHandler()
# 文件输出
fh = logging.FileHandler('test.txt', encoding='utf-8')
# 日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - 日志信息：%(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
logging.debug('debug')
logging.info('info')
logging.error('error')
logging.critical('critical')
