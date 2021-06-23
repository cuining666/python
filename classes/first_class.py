# __author: ioi
# date: 2021/6/7

class Bar:
    '''
    构造方法
    '''

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def foo(self):
        print(self.name)


b = Bar('bar', '18', 'man')
b.foo()
print(b.name, b.age, b.sex)
