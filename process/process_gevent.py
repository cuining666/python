# __author: ioi
# date: 2021/6/25
# gevent协程
import greenlet
import gevent
import time
from gevent import monkey
from urllib.request import urlopen

monkey.patch_all()  # 猴子补丁，耗时操作会使用，非耗时操作不用


def test1():
    print('12')
    gr2.switch()
    print('34')
    gr2.switch()


def test2():
    print('56')
    gr1.switch()
    print('78')


def foo():
    print('foo start', time.ctime())
    gevent.sleep(1)
    print('foo end')


def bar():
    print('bar start')
    gevent.sleep(2)
    print('bar end', time.ctime())


def f(url):
    print('GET:[%s]' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes recieved from %s' % (len(data), url))


if __name__ == '__main__':
    gr1 = greenlet.greenlet(test1)
    gr2 = greenlet.greenlet(test2)
    gr1.switch()

    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar)
    ])

    urls = ['http://english.dxsbb.com/index.html', 'https://www.imooc.com/', 'https://www.sac.net.cn/cyry/kspt/kstz/']
    start = time.time()
    print(start)
    # 串行爬取
    # for u in urls:
    #     f(u)
    # 协程爬取
    gevent.joinall([
        gevent.spawn(f, 'http://english.dxsbb.com/index.html'),
        gevent.spawn(f, 'https://www.imooc.com/'),
        gevent.spawn(f, 'https://www.sac.net.cn/cyry/kspt/kstz/')
    ])
    print(time.time() - start)
