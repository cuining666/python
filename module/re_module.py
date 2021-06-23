# __author: ioi
# date: 2021/6/4
# 正则表达式
import re

ret = re.findall('a..in', 'helloalvin')
print(ret)  # ['alvin']

ret = re.findall('^a...n', 'alvinhelloawwwn')
print(ret)  # ['alvin']

ret = re.findall('a...n$', 'alvinhelloawwwn')
print(ret)  # ['awwwn']

ret = re.findall('a...n$', 'alvinhelloawwwn')
print(ret)  # ['awwwn']

ret = re.findall('abc*', 'abcccc')  # 贪婪匹配[0,+oo]
print(ret)  # ['abcccc']

ret = re.findall('abc+', 'abccc')  # [1,+oo]
print(ret)  # ['abccc']

ret = re.findall('abc?', 'abccc')  # [0,1]
print(ret)  # ['abc']

ret = re.findall('abc{1,4}', 'abccc')
print(ret)  # ['abccc'] 贪婪匹配

# 前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
ret = re.findall('abc*?', 'abcccccc')
print(ret)  # ['ab']

# --------------------------------------------字符集[]
ret = re.findall('a[bc]d', 'acd')
print(ret)  # ['acd']

ret = re.findall('[a-z]', 'acd')
print(ret)  # ['a', 'c', 'd']

ret = re.findall('[.*+]', 'a.cd+')
print(ret)  # ['.', '+']

# 在字符集里有功能的符号: - ^ \

ret = re.findall('[1-9]', '45dha3')
print(ret)  # ['4', '5', '3']

ret = re.findall('[^ab]', '45bdha3')
print(ret)  # ['4', '5', 'd', 'h', '3']

ret = re.findall('[\d]', '45bdha3')
print(ret)  # ['4', '5', '3']

# 反斜杠后边跟元字符去除特殊功能,比如\.
# 反斜杠后边跟普通字符实现特殊功能,比如\d
# \d  匹配任何十进制数；它相当于类 [0-9]。
# \D 匹配任何非数字字符；它相当于类 [^0-9]。
# \s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
# \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
# \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
# \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
# \b  匹配一个特殊字符边界，比如空格 ，&，＃等

ret = re.findall('I\b', 'I am LIST')
print(ret)  # []
ret = re.findall(r'I\b', 'I am LIST')
print(ret)  # ['I']

# ret = re.findall('c\l', 'abc\le')
# print(ret)  # []
# ret = re.findall('c\\l', 'abc\le')
# print(ret)  # []
ret = re.findall('c\\\\l', 'abc\le')
print(ret)  # ['c\\l']
ret = re.findall(r'c\\l', 'abc\le')
print(ret)  # ['c\\l']

# -----------------------------eg2:
# 之所以选择\b是因为\b在ASCII表中是有意义的
m = re.findall('\bblow', 'blow')
print(m)
m = re.findall(r'\bblow', 'blow')
print(m)

m = re.findall(r'(ad)+', 'add')
print(m)

ret = re.search('(?P<id>\d{2})/(?P<name>\w{3})', '23/com')
print(ret.group())  # 23/com
print(ret.group('id'))  # 23

ret = re.search('(ab)|\d', 'rabhdg8sd')
print(ret.group())  # ab
