# __author: ioi
# date: 2021/6/1

status = False


def login_type(type='acc'):
    def login(func):
        def inner():
            global status
            if not status:
                username = input("用户名：").strip()
                password = input("密码：").strip()
                with open('user.txt', 'r', encoding='utf8') as f:
                    if type == 'acc':
                        for line in f:
                            if line.startswith("account:"):
                                valid(line, password, username)
                    if type == 'wx':
                        for line in f:
                            if line.startswith("weixin:"):
                                valid(line, password, username)
            else:
                print('123')

        def valid(line, password, username):
            global status
            userName = line.split(",")[0].split(":")[1].strip()
            pwd = line.split(",")[1].strip()
            if username == userName and password == pwd:
                print("Welcom,%s" % username)
                func()
                status = True
            else:
                print("username or password error")

        return inner

    return login


@login_type()
def home():
    print('This is home page...')


@login_type('wx')
def finance():
    print('This is finance page')


def book():
    print('This is book page')


finance()
