# __author: ioi
# date: 2021/6/15
# 进程数据通信
from multiprocessing import Process, Manager


def foo(dd, ll, n):
    dd[n] = 'go'
    dd['2'] = 'abc'
    dd['cb'] = None
    ll.append(n)


if __name__ == '__main__':
    with Manager() as manager:  # 主进程
        d = manager.dict()
        li = manager.list()
        p_list = []
        for i in range(10):
            p = Process(target=foo, args=(d, li, i))  # 作为参数传给子进程
            p_list.append(p)
            p.start()
        for p in p_list:
            p.join()
        print(d)
        print(li)
