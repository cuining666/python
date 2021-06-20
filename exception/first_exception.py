# __author: ioi
# date: 2021/6/10

def func(param):
    try:
        i = int(param)
    except IndexError as e:
        print(e)
    except ValueError as e:
        print("aaa", e)
    except Exception as e:
        print("bbb", e)
    else:
        print("没发生异常是执行")
    finally:
        print("无论何时都执行")


if __name__ == '__main__':
    func('as')
