# __author: ioi
# date: 2021/5/24
_user = 'cuining'
_password = '123456'
count = 0
while count < 3:
    username = input("用户名：")
    password = input("密码：")
    if username == _user and password == _password:
        print("Welcome, {}".format(username))
        break
    else:
        print("username or password is invalid")
    count += 1
    if count == 3:
        flag = input("Are you try?[y/n]")
        if flag == 'y':
            count = 0
#循环后else只在循环全部跑完时执行，break不会执行
else:
    print("Your account has been locked for 20 minutes")
