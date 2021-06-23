# __author: ioi
# date: 2021/6/23
# re常用方法
import re

# 1
re.findall('a', 'alvin yuan')  # 返回所有满足匹配条件的结果,放在列表里
# 2
re.search('a', 'alvin yuan').group()  # 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

# 3
re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配

# 4
ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']

# 5
ret = re.sub('\d', 'abc', 'alvin5yuan6', 1)
print(ret)  # alvinabcyuan6
ret = re.subn('\d', 'abc', 'alvin5yuan6')
print(ret)  # ('alvinabcyuanabc', 2)

# 6
obj = re.compile('\d{3}')
ret = obj.search('abc123eeee')
print(ret.group())  # 123

ret = re.finditer('\d', 'ds3sy4784a')
print(ret)  # <callable_iterator object at 0x10195f940>

print(next(ret).group())
print(next(ret).group())

ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['oldboy']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可

ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['www.oldboy.com']

print(re.findall("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", "<h1>hello</h1>"))
print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", "<h1>hello</h1>"))
print(re.search(r"<(\w+)>\w+</\1>", "<h1>hello</h1>"))

# 匹配出所有的整数
# ret=re.findall(r"\d+{0}]","1-2*(60+(-40.35/5)-(-4*3))")
ret = re.findall(r"-?\d+\.\d*|(-?\d+)", "1-2*(60+(-40.35/5)-(-4*3))")
ret.remove("")

print(ret)
