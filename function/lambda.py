# __author: ioi
# date: 2021/5/30
from functools import reduce

# lambda实现1到5的阶乘，计算列表乘积：1*2*3*4*5
# reduce() 函数会对参数序列中元素进行累积
print(reduce(lambda x, y: x * y, range(1, 6)))

# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# 计算列表各个元素的平方
print(list(map(lambda x: x ** 2, range(1, 6))))

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
letters = ['a', 'B', 'C', 'd', 'E', 'f', 'g']
print(list(filter(lambda x: x == x.upper(), letters)))


# 装饰器 + lambda
def calculate(flag):
    def wapper(func):
        if flag == "+":
            return lambda a, b: a + b
        elif flag == "-":
            return lambda a, b: a - b
        elif flag == "*":
            return lambda a, b: a * b
        elif flag == "/":
            return lambda a, b: a / b

    return wapper


@calculate("*")
def func(a, b):
    pass


print(func(3, 4))
