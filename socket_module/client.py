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
    data = sk.recv(1024)
    print(str(data, 'utf8'))
sk.close()
