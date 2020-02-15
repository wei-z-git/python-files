# scores = {'语文': 90, '数学': 80, '英语': 70}
# print(scores)
# empty_dict = {}
#
# dict2 = {(20, 30): 'gogo', 30: 'bad'}
# print(dict2)
#
#
# vegetables = [('黄瓜', 90), ('茄子', 59), ('西红柿', 23)]
# dict3 = dict(vegetables)
# print(dict3)
#
# dict4 = dict(a=3, b=5)
#
# print(dict4)
# print(dict4['a'])
#
# dict4['haha']=3
# print(dict4)
# del dict4['haha']
# print('dict is %s' % dict4)
# print('a' in dict4)
#
# print(dir(dict))
#
# dict4 = dict(a=3, b=5)
# print('dict is %s' % dict4)
# dict4.clear()
# print('dict is %s' % dict4)
# print(dict4.get('a'))
# print(dict4.items())
# print(dict4.keys())
# val = dict4.values()
# print(type(val))
# print(list(val))
# dict4.popitem()
# print(dict4)

#
# a = dict.fromkeys(['c', 'd'])
# print(a)

# 使用字典key给字符串中传入值
temp = '书名是：%(name)s, 价格是%(price)04.2f, 出版社是：%(publish)s'
book = {'name': '馒头历险记', 'price': 99, 'publish': '馒头社'}
print(temp % book)


