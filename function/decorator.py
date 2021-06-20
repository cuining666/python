# __author: ioi
# date: 2021/5/31
# 装饰器
'''
优点：此处有N个函数，对每个函数添加耗时计算，无需再修改这N个函数，只要新增一个函数即可
缺点：改变了调用方式，因为函数名变了，装饰器可以避免这个缺点
'''
import time


# 简单装饰器函数
def show_time(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        result = end - start
        return result

    return inner


# 有参数的功能函数的装饰器函数
def show_summ(func):
    def inner(*a, **b):
        start = time.time()
        func(*a, **b)
        end = time.time()
        result = end - start
        return result

    return inner


# 装饰器函数添加参数对功能函数区别对待
def logger(flag=''):
    def show_summ(func):
        def inner(*args):
            start = time.time()
            func(*args)
            end = time.time()
            result = end - start
            if flag == 'true':
                print("添加记录日志功能")
            return result

        return inner

    return show_summ


# @show_time等同于foo = show_time(foo)
@show_time
def foo():
    print('0')
    time.sleep(2)


# @show_time等同于foo1 = show_time(foo1)
@show_time
def foo1():
    print('1')
    time.sleep(3)


# @show_summ等同于summ = show_summ(summ)
@show_summ
def summ(*a, **b):
    sum = 0
    for val in a:
        sum += val
    for key in b:
        print('{k}:{v}'.format(v=b[key], k=key), end="~")
    print(sum)


# 只对plus函数进行日志功能
@logger('true')
def plus(*args):
    sum = 0
    for v in args:
        sum += v
    print(sum)


# 对multiply函数不添加日志功能
@logger()
def multiply(*args):
    res = 1
    for v in args:
        res *= v
    print(res)


# 方法名作为参数传入
# def show_time(func):
#     start = time.time()
#     # 使用参数直接调用函数
#     func()
#     end = time.time()
#     result = end - start
#     return result


# 此处调用方式没有改变，依旧是调用原来的函数名
print('foo耗时：%s' % foo())
print('f001耗时：%s' % foo1())
print('summ耗时：%s' % summ(1, 2, 3, name='aaa', age=18, sex='女'))
print(plus(1, 2, 3, 4, 5))
print(multiply(1, 2, 3, 4, 5))
