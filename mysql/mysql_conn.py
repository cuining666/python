# __author: ioi
# date: 2021/6/27
import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.56.102', port=3306, user='root', passwd='root', db='test', charset='utf8')
# 创建游标，将查询的结果以字典形式返回，不设置参则以元祖返回
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 插入单条
# result = cursor.execute('insert into t_item (name,stock) values (%s, %s)', ('小米11', 20))
# conn.commit()
# 打印最新插入的数据的id
# print(cursor.lastrowid)
# 插入多条
params = [
    ('华硕RTX3090', 5),
    ('微星RTX3080Ti', 5),
    ('微星RTX3070Ti', 15)
]
# results = cursor.executemany('insert into t_item (name,stock) values (%s, %s)', params)
# conn.commit()
# 打印执行条数
# print(result, results)

# 修改
# cursor.execute('update t_item set stock=%s where id=%s', (15, 10))
# conn.commit()

# 删除
# cursor.execute('delete from t_item where id=%s', (11,))
# conn.commit()

# 查询
count = cursor.execute('select * from t_item')
rss = cursor.fetchall()
# 游标重置，否则rs拉取的是None
cursor.scroll(0, mode='absolute')
rs = cursor.fetchone()
print(rss)
print(count)
print(rs)

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
