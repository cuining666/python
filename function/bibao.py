# __author: ioi
# date: 2021/5/31
# 闭包
'''
如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure)
此处inner函数就是闭包
'''
def foo():
    x = 10

    def inner():
        print(x)

    return inner


func = foo()
func()
