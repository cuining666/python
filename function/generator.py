# __author: ioi
# date: 2021/6/2
# 生成器 - 一个可迭代对象
import sys


def fibonacci(n):
    a, b, count = 0, 1, 0
    while count < n:
        # 使用了yield的函数被称为生成器
        # yield类似于return，只是return一次返回后就结束了，而yield会把值保存起来，下次从yield处继续执行
        yield a
        a, b = b, a + b
        count += 1


def func():
    print("123456")
    count = yield
    print(count)
    yield 2


c = func()
for i in range(1, 3):
    if i == 1:
        # 第一次进func生成器时send参数时None时因为还没有变量接收，所以此次要传None
        c.send(None)
    else:
        # else中的send会把参数赋给count变量
        c.send('This is count')

f = fibonacci(10)
while True:
    try:
        print(next(f), end=" ")
        # f.send(None)等同于next(f)
        # print(f.send(None), end=" ")
    except StopIteration:
        sys.exit()
