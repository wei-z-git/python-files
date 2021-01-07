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

userinfo=[
    (3,'alex'),
    (4,'tom'),
    (5,'xxx')
]
# 增加，采用executemany方法可以更快执行数据
sql='insert into t1 values(%s,%s);'
cursor.executemany(sql,userinfo)

# 删除同

client.commit()
cursor.close()
client.close()