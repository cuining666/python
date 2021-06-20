# __author: ioi
# date: 2021/6/10
# 自定义异常
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


if __name__ == '__main__':
    try:
        # 主动抛出异常
        raise CustomException('哈哈哈')
    except Exception as e:
        print(e)

    # 断言，用于强制用户服从，不服从则报错，可捕获，但一般不捕获
    assert 1 == 2
