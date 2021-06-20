# __author: ioi
# date: 2021/6/13
import socket
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
# 允许3人排队
sk.listen(5)
print('waiting...')
# 阻塞
while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
            cmd, file_name, file_size = str(data, 'utf8').split('|')
            path = os.path.join(BASE_DIR, 'upload', file_name)
            file_size = int(file_size)

            f = open(path, 'ab')
            has_recv = 0
            while has_recv != file_size:
                data = conn.recv(1024)
                f.write(data)
                has_recv += len(data)
            f.close()
        except Exception:
            # 当前客户端停了后，跳出循环链接排队中的客户端
            break
    conn.close()
