# # a_age = input("请输入您的年龄：")
# # age = int(a_age)
# # if age > 20:
# #     print("超过20了")
#
# # s_age = input("请输入您的年龄：")
# age = 99
# if age > 20 and (age < 40):
#     print("年轻人")
# elif age > 40 and (age < 50) and (age < 60):
#     print("zhongnianren")
# elif age > 50:
#     print('laoren')
#
# age = 1
# if age > 5:
#     print('haha')
# elif age < 3:
#     pass
# elif age >= 3 and (age <= 5):
#     print('haha')
#
#
# s_age = input("请输入:")
# age = int(s_age)
# assert 20 < age < 30
# print('年龄在20-30')

# a_tuple = ('a', 'cs', 'css')
# i = 0
# while i < len(a_tuple):
#     print(a_tuple[i])
#     i += 1
# print('over')


# # 对整数列表的元素分类
# src_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
# a_list = []  # 整除3
# b_list = []  # 整除3余1
# c_list = []  # 整除3余2
# i = 0
# while i < len(src_list):
#     if src_list[i] % 3 == 0:
#         a_list.append(src_list[i])
#         i += 1
#     elif src_list[i] % 3 == 1:
#         b_list.append(src_list[i])
#         i += 1
#     elif src_list[i] % 3 == 2:
#         c_list.append(src_list[i])
#         i += 1
#     else:
#         i += 1
# print('\n', a_list, '\n', b_list, '\n', c_list)

# # 计算阶乘
# s_max = input("阶乘：")
# mx = int(s_max)
# result = 1
# for i in range(1, mx+1):
#     result *= i
# print(result)


# a_truple = ('haha', 'asd', 123)
# for i in a_truple:
#     print(i)
#


# # 计算数值元素的总和
# src_list = [12, 45, 213, 4324, 13, 123, 34]
# result = 0
# my_count = 0
# for i in src_list:
#     result + i
#     my_count += 1
# print(result)

# my_dict = {'haha': 123, 'papa': 'some', 'hehe': 21}
# for key in my_dict.keys():
#     print(key)
#
# print('==================')
# for value in my_dict.values():
#     print(value)
#     # value += 1
# print('==================')

# for i in range(1, 9+1):
#     j = 0
#     while j < 3:
#         print('igg')
#         j += 1
#
# a = 'a'
# a_range = [123, 54, 21, 3423]
# a_list = [x * x for x in a_range if x == 123]
# print(a_list)
#

# a_gene = (x+x for x in range(10))
# for i in a_gene:
#     print(i, end='\n')
#
# # y能整除x 就将他们配对
# src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
# src_b = [3, 5, 7, 11]
# c_list = [(x, y) for x in src_a for y in src_b if x % y == 0]
# print(c_list)


# # zip函数
# a = ['a', 'b', 'c']
# b = [1, 2, 3]
# c = [x for x in zip(a, b)]
# print(c)

# # return 到test函数
# def test():
#     for i in range(1, 10):
#         print('i = %s' % i)
#     if i == 2:
#         # continue
#         print('i 特殊  ', i)
#         return
#     else:
#         print('else 块：', i)
#
#
# test()



