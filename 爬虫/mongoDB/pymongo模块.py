from pymongo import MongoClient


client = MongoClient('mongodb://admin:123456@192.168.1.106:27017')
# 选择数据库 db1=client.db1 或
db1 = client['db1']

# table_emp=db1.emp
table_emp = db1['emp']


rows = table_emp.find({"_id": {"$gt": 10}})
for row in rows:
    print (row)
