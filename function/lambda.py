# __author: ioi
# date: 2021/5/30
from functools import reduce

# lambda实现1到5的阶乘
print(reduce(lambda x, y: x * y, range(1, 6)))
