# python2需要注明编码，python3中默认是utf-8
# -*-coding:utf-8 -*-
# __author: ioi
# date: 2021/5/27
s = "我很好"
s_to_utf8 = s.encode("utf-8")
#utf-8转gbk
ss=s_to_utf8.decode("utf-8")
s_to_gbk=ss.encode("gbk")
#python3编码后会把内容转换为字节形式
print(s_to_utf8)
print(s_to_gbk)
#python3内容是用unicode
print(s)
