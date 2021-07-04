# __author: ioi
# date: 2021/6/15
import threading
import time

begin = time.time()


def foo(n):
    print('foo%s' % n)
    time.sleep(1)


def bar(n):
    print('bar%s' % n)
    time.sleep(2)


t1 = threading.Thread(target=foo, args=(1,))
t2 = threading.Thread(target=bar, args=(2,))
t1.start()
t2.start()
# join()等待线程执行完在执行主线程的程序
t1.join()
t2.join()
end = time.time()
print('......main process......')
print(end - begin)
