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

def fb_use_for(n):
    before, after = 0,1
    # _ 只是一个占位符，只在乎遍历次数range(n)就是遍历n次。
    # for _in range(n)和for each in range(n)是一样的，只不过_在下面不会用到，这里的_可以替换成任何符合规定的字符串
    for _ in range(n):
        yield before
        before, after = after, before + after


def feibo(n):
    if n <= 2:
        return n - 1
    return feibo(n - 1) + feibo(n - 2)


if __name__ == '__main__':
    print(feibo(8))
    fb(8)
    print()
    for i in fb_use_for(8):
        print(i)