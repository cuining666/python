# __author: ioi
# date: 2021/5/24
_user = 'cuining'
_password = '123456'
for i in range(3):
    username = input("用户名：")
    password = input("密码：")
    if username == _user and password == _password:
        print("Welcome, {}".format(username))
        break
    else:
        print("username or password is invalid")
else:
    print("Your account has been locked for 20 minutes")
