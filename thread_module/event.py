# __author: ioi
# date: 2021/6/19
# 事件
import threading
import time


class Boss(threading.Thread):
    def run(self):
        print('BOSS:今天大家都要加班')
        # 把event标志位设置成True, 激活wait
        event.set()
        time.sleep(5)
        print('BOSS:今天大家辛苦了，可以下班了')
        event.is_set() or event.set()


class Worker(threading.Thread):
    def run(self):
        event.wait()
        print('Worker:又要加班啊！')
        time.sleep(1)
        # 把event标志位设置成False, wait阻塞
        event.clear()
        event.wait()
        print('Worker:下班啦！')


if __name__ == '__main__':
    event = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
