# # my_list = ['haha', 3, 'some', 'gogo', 'cc']
# # print(my_list)
# # my_tuple = ('gogo', 34, 'ok')
# # # print(my_tuple[0])
# #
# # # print(my_list[0])
# #
# # # print(my_list[0:-4:1])
# #
# # a_truple = (1, 20, 3)
# # b_truple = ('c', 20, '4')
# # # sum_truple = a_truple * 3
# # print(max(a_truple))
#
# vals = 'a', 'b', 'c'
# # print(vals)
#
# # *a, c = vals
# # print(a)
# #
# # a = tuple(range(1,10,2))
# # print(a)
# ran = range(1, 5, 2)
# ll = list(range(1, 5, 2))
# trup = tuple(ll)
# print('range is %s', ran)
# print('list is ', ll)
# print(trup)


# a_list = [0, 'ss', 123, [123, 456]]
# aa_append = ['haha', 0]
# a_list.insert(1, aa_append)
# print(a_list)
# del a_list[2:3]
# print(a_list)
# a_list.remove(0)
# print(a_list)
# # a_list.clear()
# # print(a_list)
#
# a_list[2] = 'wode'
# print(a_list)

# del a_list
# print(a_list)

# a_list = list(range(1, 10))
# print('a_list : ', a_list)
# a_list[2:9:2] = ('a', 'b', 'c', 'd')
# print('a_list : ', a_list)
# c = a_list.count('a')
# print(c)
# # index method
# c = a_list.index('a', 0, 20)
# print(c)

# # 栈操作
# stack = []
# stack.append('m1')
# stack.append('m2')
# stack.append('m3')
# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack)


a_list = ['abccc', 'abc', 'abcd']
a_list.sort(key=len)
print(a_list)

