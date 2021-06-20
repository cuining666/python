# __author: ioi
# date: 2021/6/8
class Province:
    """
    省份类
    """
    # 静态地段
    country = 'China'

    # 构造方法
    def __init__(self, name):
        # 普通字段
        self.name = name

    # call方法，对象()，类()()默认调用此方法
    def __call__(self, *args, **kwargs):
        print('call')

    # int()
    def __int__(self):
        return 1

    # str()，类似于java的toString方法
    def __str__(self):
        return '%s-%s' % (self.name, self.country)

    # add()，类似于java的toString方法
    def __add__(self, other):
        return '%s-%s' % (self.name, other.name)

    def __getitem__(self, item):
        print(item, type(item))
        if type(item) == slice:
            print('切片检索', item.start, item.stop, item.step)
        else:
            print('索引检索', item)

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)

    """
    如果类中有__iter__方法，则对象是可迭代对象
    """

    def __iter__(self):
        # 返回迭代器
        return iter([1, 2, 3, 4, 5, 6])

    """
    析构方法
    """

    def __del__(self):
        print('垃圾回收（对象自动销毁时）是触发')

    # 普通方法
    def show_name(self):
        print(self.name)

    # 静态方法
    @staticmethod
    def static_foo():
        print('static function')

    # 静态方法
    @staticmethod
    def static_foo1(a, b):
        print(a, b)

    # 类方法，不常用
    @classmethod
    def class_foo(cls):
        print(cls)
        print('class function')

    # 属性，介于方法和字段之间，类似于java中的getter
    @property
    def prop(self):
        print('property')
        return True

    # 类似于java中的setter，方法名要和有装饰器@property的方法名一致
    @prop.setter
    def prop(self, val):
        print(val)

    @prop.deleter
    def prop(self):
        print('deleter')

    # 属性的另外一种写法start
    def f1(self):
        print('f1')
        return 'f1'

    def f2(self, val):
        print('f2')
        return val

    def f3(self):
        print('f3')

    per = property(fget=f1, fset=f2, fdel=f3)
    # 属性的另外一种写法end


if __name__ == '__main__':
    p = Province('Shanghai')
    # 静态字段可以通过类访问，也可以通过对象访问
    print(Province.country)
    print(p.name, p.country)
    # 普通方法可以通过对象和类调用，类调用必须传入对象（不推荐）
    p.show_name()
    Province.show_name(p)
    # 静态方法只能通过类调用
    Province.static_foo()
    Province.static_foo1('a', 'b')
    # cls参数不用传，自动的是类名
    Province.class_foo()
    # 调用属性不需要括号
    b = p.prop
    print('return', b)
    # 对应调用装饰器@prop.setter的方法
    p.prop = False
    # 对应调用装饰器@prop.deleter的方法
    del p.prop

    # 属性的另外一种写法
    c = p.per
    print(c)
    p.per = 1
    del p.per

    # 调用__call__特殊方法
    p()
    Province('Jiangsu')()
    # 调用__int__特殊方法
    i = int(p)
    print(i)
    # 调用__str__特殊方法
    s = str(p)
    print(p)  # Shanghai-China
    print(s)  # Shanghai-China

    p1 = Province('Shandong')
    p2 = Province('Anhui')
    # 调用__add__方法，第一个参数是p1，第二个参数是p2
    result = p1 + p2
    print(result)

    # 打印P1中的字段内容
    print(p1.__dict__)
    # 打印类中的所有内容
    print(Province.__dict__)

    li = Province('Liaoning')
    # 调用__getitem__方法
    li[8]
    qp = li[1:4:2]
    # 调用__setitem__方法
    li[100] = 'shengyang'
    # 调用__delitem__方法
    del li[999]

    # 创建li时自动调用__iter__方法，返回迭代器
    for i in li:
        print(i)
"""
如果对象中需要保存一些值，执行某功能时，需要使用对象的值，此时使用普通方法
如果不需要任何对象中的值，此时使用类方法，类似于函数
"""
