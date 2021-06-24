# __author: ioi
# date: 2021/6/15
# 多进程
import multiprocessing
import time
import os


def foo(n):
    time.sleep(1)
    print('foo%s' % n)


def info(title):
    print(title)
    print('module_name', __name__)
    print('parent pid:', os.getppid())
    print('pid:', os.getpid())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = multiprocessing.Process(target=foo, args=(i,))
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()

    info('main process running...')
    print('等待3s...')
    time.sleep(3)
    p = multiprocessing.Process(target=info, args=('bob',))
    p.start()
    p.join()
    print('all processes end...')
