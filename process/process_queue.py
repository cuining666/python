# __author: ioi
# date: 2021/6/15
# 进程数据通信
from multiprocessing import Process, Queue


def foo(cq, n):
    cq.put([42, n, 'foo'])


if __name__ == '__main__':
    q = Queue()  # 主进程
    for i in range(3):
        p = Process(target=foo, args=(q, i))  # 作为参数传给子进程
        p.start()
    print(q.get())
    print(q.get())
    print(q.get())
