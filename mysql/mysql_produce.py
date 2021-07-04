# __author: ioi
# date: 2021/7/1
import pymysql

# 执行存储过程，获取存储过程的结果集
conn = pymysql.connect(host='192.168.56.102', port=3306, user='root', passwd='root', db='test', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
r = cursor.callproc('p1', args=(1, 2, 3, 4))
print(r)
result = cursor.fetchall()
print(result)

# 获取执行完存储的参数
r1 = cursor.execute("select @_p1_0,@_p1_1,@_p1_2,@_p1_3")
print(r1)
result1 = cursor.fetchall()
print(result1)
