# Author: ioi
# Create date: 2023-09-01 20:48
# 三目运算
a, b = 1, 2
c = a if a < b else b
print(c)

# 四位数的百位+十位+个位大于10，则返回True
num = int(input("请输入4位数字："))
if len(str(num)) != 4:
    print("输入数字非法，请重新输入！")
else:
    if num // 100 % 10 + num // 10 % 10 + num % 10 > 10:
        print("True")
    else:
        print("False")
