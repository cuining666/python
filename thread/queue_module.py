# __author: ioi
# date: 2021/6/19
# 队列
import threading
import queue
import time
import random


class Producer(threading.Thread):
    def run(self):
        while True:
            val = random.randint(0, 100)
            q.put(val)
            print('生产产品', val)
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        while True:
            print('购买产品', q.get())


if __name__ == '__main__':
    # 参数不送默认是队列容量无限大
    q = queue.Queue()
    threads = [Producer(), Producer(), Producer(), Producer(), Producer(), Consumer()]
    for t in threads:
        t.start()
