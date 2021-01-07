import pymysql

client = pymysql.connect(
    host='192.168.1.106',
    port=3306,
    user='root',
    password='qiang666',
    database='db6',
    charset='utf8'
)
# 游标.pymysql.cursors.DictCursor以字典形式把表头也显示出来
cursor = client.cursor(pymysql.cursors.DictCursor)


sql = "select * from user where id >3;"

rows = cursor.execute(sql)
try:
    cursor.execute(sql_1)  
    cursor.execute(sql_2)  
    cursor.execute(sql_3)  
except Exception as e:
    connect.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    connect.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)# 关闭连接
cursor.close()
connect.close()

pymysql实现事务处理