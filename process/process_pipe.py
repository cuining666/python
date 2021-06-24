# __author: ioi
# date: 2021/6/15
# 进程数据通信
from multiprocessing import Process, Pipe


def foo(conn):
    conn.send('子进程 to 主进程')
    print(conn.recv())


if __name__ == '__main__':
    main_conn, child_conn = Pipe()  # 主进程
    for i in range(3):
        p = Process(target=foo, args=(child_conn,))  # 把通道作为参数传给子进程
        p.start()
    print(main_conn.recv())
    main_conn.send('主进程 to 子进程')
