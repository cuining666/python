# __author: ioi
# date: 2021/6/3
# 随机
import random

print(random.random())  # (0,1)----float

print(random.randint(1, 3))  # [1,3]

print(random.randrange(1, 3))  # [1,3)

print(random.choice([1, '23', [4, 5]]))  # 23

print(random.sample([1, '23', [4, 5]], 2))  # 列表中随机取2个返回列表

print(random.uniform(1, 3))  # 产生1到3之间的随机浮点数，区间可以不是整数

item = [1, 3, 5, 7, 9]
# 将序列的所有元素随机排序
random.shuffle(item)
print(item)


def v_code():
    code = ''
    for i in range(5):
        num = random.randint(0, 9)
        alf = chr(random.randint(65, 90))
        add = random.choice([num, alf])
        code += str(add)
    return code


print(v_code())
