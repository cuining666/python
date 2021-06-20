# __author: ioi
# date: 2021/6/10
# 反射，通过字符串的形式操作对象中的成员

import module


class Foo():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('%s-%s' % (self.name, self.age))


if __name__ == '__main__':
    foo = Foo('xiaohai', 17)
    # 获取指定字段
    val = getattr(foo, 'name')
    print(val)
    # 获取指定方法
    func = getattr(foo, 'show')
    print(func)
    func()
    # 判断对象中是否有指定字段或方法
    flag = hasattr(foo, 'age')
    print(flag)
    # 新增/更新对象中的字段
    setattr(foo, 'k', 'v')
    setattr(foo, 'name', 'dabing')
    print(foo.k, foo.name)
    # 删除对象中的字段
    # delattr(foo, 'name')
    # print(foo.name)

    # 模块级别反射
    s = getattr(module, 'NAME')
    print(s)
    ff = getattr(module, 'func')
    print(ff)
    ff()
    # 反射模块中的类
    cls = getattr(module, 'C')
    c = cls('123')
    print(c.aaa)
