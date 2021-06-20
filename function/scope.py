# __author: ioi
# date: 2021/5/30
'''
变量查找顺序：LEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；
只有模块、类、及函数才能引入新作用域；
对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；
内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字。nonlocal是python3新增的关键字，有了这个 关键字，就能完美的实现闭包了。
'''
count = 10


def foo():
    # 全局变量在函数内使用需加global关键字
    global count
    count = 5
    i = 10

    def foo1():
        # 外层变量在内层函数中使用需加nonlocal关键字
        nonlocal i
        i = 8

    foo1()
    print(i)


foo()
print(count)
