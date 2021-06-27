# __author: ioi
# date: 2021/6/25
# yield协程
def consumer(name):
    print('start...')
    while True:
        new_prod = yield
        print('[%s] is eating product [%s]' % (name, new_prod))


def producer():
    next(con1)
    next(con2)
    for i in range(5):
        print('[producer] is making product [%s]' % (i + 1))
        con1.send(i + 1)
        con2.send(i + 1)


if __name__ == '__main__':
    con1 = consumer('test1')
    con2 = consumer('test2')
    producer()
