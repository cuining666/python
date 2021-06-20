# __author: ioi
# date: 2021/5/30
def digui(n):
    if n > 1:
        result = n * digui(n - 1)
    else:
        result = n
    return result


num = digui(1)
print(num)
