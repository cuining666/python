# __author: ioi
# date: 2021/6/7

class Bar:
    '''
    构造方法
    '''
    # 私有属性: 最前面是__，一般只能在类内使用，在类外调用是_Bar__birthday
    __birthday = ""

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 私有方法
    def __func(self):
        print("私有方法")

    def foo(self):
        self.__func()
        print(self.name)


b = Bar('bar', '18', 'man')
b.foo()
print(b.name, b.age, b.sex)
