# __author: ioi
# date: 2021/8/7
# 被测程序
class Clac:
    def add_func(self, x, y, *d):
        result = x + y
        for i in d:
            result += i
        return result

    def sub_func(self, x, y, *d):
        result = x - y
        for i in d:
            result -= i
        return result

    @classmethod
    def mul_func(cls, x, y, *d):
        result = x * y
        for i in d:
            result *= i
        return result

    @staticmethod
    def div_func(x, y, *d):
        if y != 0:
            result = x / y
        else:
            return -1
        for i in d:
            if i != 0:
                result /= i
            else:
                return -1
        return result
