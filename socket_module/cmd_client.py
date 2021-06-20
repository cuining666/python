# __author: ioi
# date: 2021/6/13

import socket

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.connect(address)
while True:
    # 阻塞
    inp = input(">>>")
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    result_len = int(str(sk.recv(1024), 'utf8'))
    sk.send(bytes('ok', 'utf8'))
    print(result_len)
    data = bytes()
    while len(data) != result_len:
        recv = sk.recv(1024)
        data += recv
    print(str(data, 'gbk'))
sk.close()
