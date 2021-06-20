# __author: ioi
# date: 2021/6/13
import socket
import subprocess

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
            # subprocess.Popen开辟多进程，stdout=subprocess.PIPE把子进程的内容合到主进程中
            s = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
            # windows下执行命令是GBK编码的，所以在客户端最后要用GBK解码
            cmd_result = s.stdout.read()
            ruslt_len = bytes(str(len(cmd_result)), 'utf8')
            conn.sendall(ruslt_len)
            # 两个send在一起会出现粘包
            # 解决粘包现象
            conn.recv(1024)
            conn.sendall(cmd_result)
        except Exception:
            # 当前客户端停了后，跳出循环链接排队中的客户端
            break
    conn.close()
