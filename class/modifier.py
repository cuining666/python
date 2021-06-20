# __author: ioi
# date: 2021/6/9
# 修饰符

class Father:
    def __init__(self):
        self.name = 'haha'
        self.__sex = 'female'


class Son(Father):
    def __init__(self, same):
        super(Son, self).__init__()
        self.same = same
        self.__favourite = 'pingpang'

    '''
    私有方法
    '''
    def __f(self):
        print(self.same)
        print(self.name)

    def foo(self):
        # 调用私有方法
        self.__f()
        print(self.__favourite)
        # 私有字段无法访问是python在前面加了前缀，只要知道前缀就可以访问，不推荐
        print(self._Father__sex)
        # 子类无法访问父类的私有字段
        print(self.__sex)


if __name__ == '__main__':
    son = Son('gggg')
    son.foo()
