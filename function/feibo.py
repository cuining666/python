# __author: ioi
# date: 2021/5/30
# 斐波那契数列
# 0 1 1 2 3 5 8 13 21 34 55 89

def fb(n):
    count, before, after = 0, 0, 1
    while count < n:
        print(before, end="\t")
        before, after = after, before + after
        count += 1


def feibo(n):
    if n <= 2:
        return n - 1
    return feibo(n - 1) + feibo(n - 2)


print(feibo(8))
fb(8)
