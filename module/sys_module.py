# __author: ioi
# date: 2021/6/3
# 访问于python解释器紧密相关的变量和函数
import sys
import time

print(sys.argv)  # 命令行参数List，第一个元素是程序本身路径
print(sys.version)  # 获取Python解释程序的版本信息
print(sys.path)  # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform)  # 返回操作系统平台名称
# sys.exit(0)  # 退出程序，正常退出时exit(0)

for i in range(10):
    sys.stdout.write('#')
    time.sleep(1)
    sys.stdout.flush()
