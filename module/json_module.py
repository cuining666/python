# __author: ioi
# date: 2021/6/5
# JSON
import json

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
print(type(dic))  # <class 'dict'>

j = json.dumps(dic)
print(type(j))  # <class 'str'>

f = open('序列化对象', 'w')
f.write(j)  # -------------------等价于json.dump(dic,f)
f.close()
# -----------------------------反序列化<br>

f = open('序列化对象')
data = json.loads(f.read())  # 等价于data=json.load(f)
print(type(data))

dct = '{"1":"111"}'
# dct = "{'1':'111'}" #json不认单引号
print(json.loads(dct))
