# # 第一题
# print('请输入字符串')
# (a, b) = input()
#
# my_tuple = (a, b)
# my_tuple3 = my_tuple * 3
# print(my_tuple3)
#
# my_tuple_plus = my_tuple3 + ('fkjava', 'crazyit')
# print(my_tuple_plus)

#
# # # 第二题
# # a_list = ['a', 123, 'b']
# # b_list = [1, 2, 3]
# # b_list[0] = a_list[0]
# # b_list[1] = a_list[1]
# # b_list[2] = a_list[2]
# # print(b_list)
# #
# #
# # 给定一个list
# list1 = ["fkjava", "crazyit", "hello", "world", "python"]
# start, end = int(input("输入start:")), int(input("输入end:"))
# # 复制
# list2 = list1[start: end]
# print(list2)


# # 第三题
# print('输入 n :')
# n = int(input())
# a_list = list(range(1, n+1))
# print(a_list)


# #  第六题
# length = int(input("请输入列表的长度:"))
# my_list = []
# for i in range(length):
#     my_list.append(input('请输入字符串:'))
# print(my_list)
#
# # 另一种方法
# new_list = list(dict.fromkeys(my_list).keys())  # 为list中每一个的元素赋一个key
# print(dict.fromkeys(my_list))  # 从list中将list作为key，因为key唯一，所以重复key只取一个
# print(dict.fromkeys(my_list).keys())  # 取到的key-value重新获取其key，返回dict_keys(['ads', 'd', 'asd'])
# print(new_list)

# # 第7题
#
# my_tuple = tuple(input("请输入多个整数:").split())  # split 分割多个整数
# hash_tuple = hash(my_tuple)
# print(my_tuple)
# print(hash_tuple)

