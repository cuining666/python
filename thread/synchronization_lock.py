# __author: ioi
# date: 2021/6/18
# 同步锁
import threading
import time


def reduce_num():
    global num
    # 在数据处理时上锁，如果不上锁，由于线程切换，导致结果错误
    r.acquire()
    temp = num
    time.sleep(0.0001)
    num = temp - 1
    r.release()


num = 100
threads = []
# 同步锁
r = threading.Lock()
for i in range(100):
    t = threading.Thread(target=reduce_num)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('result = %s' % num)
