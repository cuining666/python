# __author: ioi
# date: 2021/6/8
# 分页
class Pagination:
    def __init__(self, current_page):
        try:
            pa = int(current_page)
        except Exception as e:
            pa = 1
        self.page = pa

    @property
    def start(self):
        val = (self.page - 1) * 10
        return val

    @property
    def end(self):
        val = self.page * 10
        return val


if __name__ == '__main__':
    li = []
    for i in range(1000):
        li.append(i)
    while True:
        p = input("当前页：")
        page = Pagination(p)
        # 此处更适合字段写法，好看不用加括号
        print(li[page.start:page.end])
