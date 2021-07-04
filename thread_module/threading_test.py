# __author: ioi
# date: 2021/6/17
import threading
from time import ctime, sleep


def music(func):
    for i in range(2):
        print(threading.current_thread())
        print('Begin listening %s-%s' % (func, ctime()))
        sleep(2)
        print('End listening %s-%s' % (func, ctime()))


def movie(func):
    for i in range(2):
        print(threading.current_thread())
        print('Begin watching %s-%s' % (func, ctime()))
        sleep(3)
        print('End watching %s-%s' % (func, ctime()))


threads = []
t1 = threading.Thread(target=music, args=('都选C',))
t2 = threading.Thread(target=movie, args=('当幸福来敲门',))
threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
    # setDaemon(True)守护线程，哪个子线程设置了该方法，该子线程会和主线程一起结束，没有被主线程守护的线程会继续执行，放在start()前
    t2.setDaemon(True)
    for t in threads:
        t.start()

    # 等待子线程执行完在执行主线程的程序，放在start()后
    # t1.join()
    # t2.join()
    print(threading.current_thread())
    # 运行中的线程数
    print(threading.active_count())
    print('......main thread_module end......')
