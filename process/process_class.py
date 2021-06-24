# __author: ioi
# date: 2021/6/15
# 多进程
from multiprocessing import Process
import time


class MyProcess(Process):

    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        time.sleep(2)
        print(self.name)


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = MyProcess()
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
    print('end')
