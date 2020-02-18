# """
#     直接选择排序法
#
# """
#
#
# def get_list(x):
#     for j in range(0, len(x)-1):
#         for i in range(0, len(x)-1):
#             if x[i] > x[i+1]:
#                 t = x[i+1]
#                 x[i+1] = x[i]
#                 x[i] = t
#                 i += 1
#             else:
#                 i += 1
#         j += 1
#     return x
#
#
# x = [3, 2, 1, 24, 4124, 43, 213, 43]
# print(get_list(x))
# # print(len(x))

#
# """
# 判断是否为闰年
# """
#
#
# def is_leap(year):
#     if year % 4 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_leap(42))

#
# """
# 判断多少个数字，多少英文
# """

#
# def count_str_char(string):
#     char_num, digit_num, space_num, other_num = 0, 0, 0, 0
#     for c in string:
#         if c.isdigit():
#             digit_num += 1
#         elif c.isalpha():
#             char_num += 1
#         elif c.isspace():
#             space_num += 1
#         else:
#             other_num += 1
#     return char_num, digit_num, space_num, other_num
#
#
# string = input("请输入一个字符串:")
# if string == 'exit':
#     import sys
#     sys.exit(0)
#
# char_num, digit_num, space_num, other_num = count_str_char(string)
# print('字母个数', char_num)
# print('数字个数', digit_num)
# print('空白个数', space_num)
# print('其他字母个数', other_num)


# def lifang(x):
#     return x*x*x
#
#
# def fn(n):
#
#     result = 0
#     for i in range(1, n+1):
#         result += lifang(i)
#     print(result)
#     return result
#
#
# fn(1)
#
#
# def fn(n):
#     result = 0
#     for i in range(1, n+1):
#         result += i
#     return result
#
#
# print(fn(3))

# 接受一个list 让她剔除重复元素
# def fn(n):
#     for i in range(len(n)-1):
#         for j in range(i+1, len(n)-1):
#             if n[i] == n[j+1]:
#                 n.pop(j+1)
#
#     return n
# def fn(n):
#     n2 = []
#     for i in n:
#         if i not in n2:
#             n2.append(i)
#     print(n2)
#     return n2

# # 用set做剔除和排序
# # def fn(n):
# #     return list(set(n))


# x = [1, 2, 3, 1, 1, 123, 123]

# fn(x)

# # 生成n个不重复的0-100的元组
# import random

# n = int(input("请输入:"))


# def fn(n):
#     x = []
#     i = 1
#     print(n)
#     while i <= n:
#         num = random.randint(0, 100)
#         if num not in x:
#             x.append(num)
#             i += 1
#     return tuple(x)


# print(fn(n))

# print(chr(6))
def fn():
    