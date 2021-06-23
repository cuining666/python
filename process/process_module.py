# __author: ioi
# date: 2021/6/15
# 多进程
import multiprocessing
import time


def foo(n):
    time.sleep(1)
    print('foo%s' % n)


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = multiprocessing.Process(target=foo, args=(i,))
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
    print('end')
