# __author: ioi
# date: 2021/5/30
from functools import reduce


def foo(x, y):
    return x + y


print(reduce(foo, range(1, 101)))
