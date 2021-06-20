# __author: ioi
# date: 2021/6/12
# 单例模式
class Singleton:
    __singleton = None

    @classmethod
    def get_instance(cls):
        if cls.__singleton:
            return cls.__singleton
        else:
            cls.__singleton = Singleton()
            return cls.__singleton


if __name__ == '__main__':
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()
    print(s1 == s2)
