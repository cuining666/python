# __author: ioi
# date: 2021/6/7
import extends


class Sonn(extends.Father):
    def run(self):
        print('跑步')


if __name__ == '__main__':
    sonn = Sonn()
    sonn.run()
    sonn.work()
