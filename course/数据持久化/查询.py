# import pymysql

# client = pymysql.connect(
#     host='192.168.1.106',
#     port=3306,
#     user='root',
#     password='qiang666',
#     database='db6',
#     charset='utf8'
# )
# # 游标
# cursor = client.cursor()

# inp_user=input('输入用户名：')
# inp_pwd=input('请输入密码：')

# sql="select * from user where name=%s and pwd=%s;"
# print(sql)
# # 有值，则表示有行数，则登录成功
# rows=cursor.execute(sql,(inp_user,inp_pwd))
# if rows:
#     print('登录成功')
# else:
#     print('登陆失败')

# cursor.close()
# client.close()

# 查询并取得值
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

# 执行完结果给到管道里了
# print(rows)


# print(cursor.fetchall())
# 2、 fetchmany指定要拿的记录数量
# print(cursor.fetchmany(1))
# print(cursor.fetchone())


# 3、指定游标位置
cursor.scroll(0, mode='absolute')  # 绝对位置移动，基于最开始位置，移动指针
print(cursor.fetchone())
cursor.close()
client.close()
