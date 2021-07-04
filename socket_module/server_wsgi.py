# __author: ioi
# date: 2021/7/4
from wsgiref.simple_server import make_server
import time


def routers():
    result = (('/now', now_page),)
    return result


def now_page(request):
    f = open('index.html', 'rb')
    current_time = time.ctime(time.time())
    data = f.read()
    data = data.decode('utf8').replace('!now!', current_time)
    return [data.encode('utf8')]


def application(env, res):
    """
    env封装了所有请求信息
    res封装了所有相应信息
    """
    res('200 OK', [('Content-Type', 'text/html')])
    path = env['PATH_INFO']
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(env)
    else:
        return ['<h1>404 Not Found</h1>'.encode('utf8')]


httpd = make_server('127.0.0.1', 8000, application)
print('Serving HTTP on port 8000...')
# 开启监听HTTP请求
httpd.serve_forever()
