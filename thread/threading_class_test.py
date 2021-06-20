# __author: ioi
# date: 2021/6/17
# 死锁，递归锁
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def doFunctionA(self):
        # lock1.acquire()
        lock.acquire()
        print(self.name, '方法A执行1', time.ctime())
        time.sleep(2)
        # lock2.acquire()
        lock.acquire()
        print(self.name, '方法A执行2', time.ctime())
        # lock2.release()
        # lock1.release()
        lock.release()
        lock.release()

    def doFunctionB(self):
        # lock2.acquire()
        lock.acquire()
        print(self.name, '方法B执行3', time.ctime())
        time.sleep(3)
        # lock1.acquire()
        lock.acquire()
        print(self.name, '方法B执行4', time.ctime())
        # lock1.release()
        # lock2.release()
        lock.release()
        lock.release()

    def run(self):
        self.doFunctionA()
        self.doFunctionB()


class MyThreadB(threading.Thread):

    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(3)
            semaphore.release()


if __name__ == '__main__':
    """
    死锁
    ('MainThread', 1) 方法A执行1 Fri Jun 18 22:30:22 2021
    ('MainThread', 1) 方法A执行2 Fri Jun 18 22:30:24 2021
    ('MainThread', 1) 方法B执行3 Fri Jun 18 22:30:24 2021
    ('MainThread', 2) 方法A执行1 Fri Jun 18 22:30:24 2021
    到这就卡住了
    """
    # lock1 = threading.Lock()
    # lock2 = threading.Lock()

    # 递归锁
    lock = threading.RLock()
    threads = []
    for i in range(5):
        t = MyThread((threading.currentThread().name, i + 1))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    # 信号量
    semaphore = threading.BoundedSemaphore(5)
    threadbs = []
    for i in range(23):
        t = MyThreadB()
        t.start()
        threadbs.append(t)
    for t in threadbs:
        t.join()
