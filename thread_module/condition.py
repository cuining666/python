# __author: ioi
# date: 2021/6/19
# 条件同步
import threading
import time
import random


class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val = random.randint(0, 100)
            if lock.acquire():
                L.append(val)
                print('生产者', self.name, '：创建', str(L[len(L) - 1]), L)
                # 激活在等待中的线程
                lock.notify()
                lock.release()
            time.sleep(4)


class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
            lock.acquire()
            if len(L) == 0:
                lock.wait()
            print('消费者', self.name, '：消费', str(L[0]), L)
            del L[0]
            lock.release()
            time.sleep(1)


if __name__ == '__main__':
    L = []
    lock = threading.Condition()
    threads = []
    for i in range(5):
        p = Producer()
        p.start()
        threads.append(p)
    c = Consumer()
    c.start()
    threads.append(c)
    for t in threads:
        t.join()
    print('......All threads end......')
