# __author: ioi
# date: 2021/6/27
# 动态导入模块
import importlib

module_path = 'reflection.module'
m = importlib.import_module(module_path)
f = getattr(m, 'func')
f()
