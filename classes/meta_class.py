# __author: ioi
# date: 2021/6/10
# 祖宗类

class MyType(type):
    """
    MyType里的self是Foo类
    """
    def __init__(self, what, bases=None, dict=None):  # 1.2
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):  # 2.2
        obj = self.__new__(self, *args, **kwargs)  # 2.3
        self.__init__(obj)  # 3.1


class Foo(object, metaclass=MyType):  # 1.1
    """
    object是一切类的基类
    Foo里的self是foo对象
    """
    def __init__(self, name):  # 3.2
        self.name = name

    def __new__(cls, *args, **kwargs):  # 2.4
        return object.__new__(cls, *args, **kwargs)


foo = Foo()  # 2.1
"""
整个完整的执行流程为：1.1-1.2-2.1-2.2-2.3-3.1-3.2
"""
