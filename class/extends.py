# __author: ioi
# date: 2021/6/7
# 继承

class Father:
    def learn(self):
        print('学习')

    def work(self):
        print('工作')


class Son(Father):
    def paly(self):
        print('打游戏')

    def work(self):
        # 执行父类中的work方法
        super(Son, self).work()
        # 等同于super(Son, self).work()，推荐用super
        # Father.work(self)
        print("工作一团乱")


if __name__ == '__main__':
    son = Son()
    son.learn()
    son.paly()
    son.work()
    print()
    father = Father()
    father.work()
