# __author: ioi
# date: 2021/6/13
import os
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.connect(address)
while True:
    # 阻塞
    inp = input(">>>").strip()  # post|11.jpg
    if inp == 'exit':
        break
    cmd, path = inp.split('|')
    path = os.path.join(BASE_DIR, path)
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    file_info = 'post|%s|%s' % (file_name, file_size)
    sk.sendall(bytes(file_info, 'utf8'))

    f = open(path, 'rb')
    has_sent = 0
    while has_sent != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
    f.close()
    print('上传成功')
sk.close()
