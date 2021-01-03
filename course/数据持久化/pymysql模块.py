import pymysql

client = pymysql.connect(
    host='192.168.1.106',
    port=3306,
    user='root',
    password='qiang666',
    database='db6',
    charset='utf8'
)
# 游标
cursor = client.cursor()

sql='insert into t1 values(1,"egon");'
cursor.execute(sql)

client.commit()
cursor.close()
client.close()