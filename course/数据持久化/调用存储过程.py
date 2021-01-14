import pymysql

client = pymysql.connect(
    host='192.168.1.106',
    port=3306,
    user='root',
    password='qiang666',
    database='db6',
    charset='utf8'
)
cursor = client.cursor(pymysql.cursors.DictCursor)
res=cursor.callproc('p3',(3,111))
# 拿结果
print(cursor.fetchall())
# 查看返回值
cursor.execute('select @_p3_1')
print(cursor.fetchone())
cursor.close()
client.close()

# 附录：p3存储过程
# CREATE DEFINER=`root`@`%` PROCEDURE `p4`(
# in n int,
# out res int
# )
# BEGIN
# 	SELECT * FROM blog WHERE id > 3;
# 	SET res = 0;
# END