# __author: ioi
# date: 2021/6/13
import socket

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
# 允许3人排队
sk.listen(3)
print('waiting...')
# 阻塞
while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
            print('......', str(data, 'utf8'))
            if not data:
                break
            inp = input(">>>")
            # python3 send参数必须转为bytes
            conn.send(bytes(inp, 'utf8'))
        except Exception:
            # 当前客户端停了后，跳出循环链接排队中的客户端
            break
    conn.close()
