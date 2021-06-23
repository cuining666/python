# __author: ioi
# date: 2021/6/7

class Root:
    def a(self):
        print("Root.a")


class F(Root):
    def a1(self):
        print("F.a")


class F1(F):
    def a1(self):
        print("F1.a")

    def b(self):
        print("F1.b")


class F2(Root):
    def a(self):
        print("F2.a")

    def a2(self):
        self.b()
        print("F2.a2")

    def b(self):
        print("F2.b")


class Son(F1, F2):
    def foo(self):
        pass


if __name__ == '__main__':
    '''
    多继承优先找左侧父类的同名方法，如果多个父类有共同的根时，根最后执行
    '''
    s = Son()
    s.a()
    '''
    左边没有a2方法，右边a2方法有self.b()，此时又回到子类从新到F1中找b方法
    '''
    s.a2()
