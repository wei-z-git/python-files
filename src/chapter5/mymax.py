#
#
# def my_max():
#     """
#     获得个数值
#
#     my_max(x, y)
#         asd
#     :return:0
#     """
#
#     # 定义一个变量
#     z = x if x > y else y
#     # 返回变量z的值
#     return z
#
#
# # help(my_max)
# print(my_max.__doc__)
#


# # 递归
# def f(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 4
#     else:
#         return 2 * f(n-1) + f(n-2)
#
#
# a = f(10)
# print(a)


# def printtriangle(char, height = 5):
#     for i in range(1, height + 1):
#         for j in range(height - 1):
#             print(' ', end='')
#         for j in range(2*i-1):
#             print(char, end='')
#         print()
#
#
# printtriangle('@', 6)
# printtriangle(char=']')
# printtriangle('\\', height=8)

#
# def test(a, *books):
#     print(books)
#     for b in books:
#         print(b)
#     print(a)
#
#
# test(5, '疯狂', '疯狂anr')

# # 加俩* 传入多个关键字参数
# def test(num, *books, **haha):
#     print(books)
#     for b in books:
#         print(b)
#     print(num)
#     print(haha)
#
#
# test(123, 'ga', 123, cc=2, hahas=3)

# # 逆向参数收集
# def test(name, message):
#     print('用户名：', name)
#     print('信息：', message)
#
#
# my_list = ('馒头', '熟的')
# test(*my_list)

#


# # 字典逆向收集
# def bar(book, price, desc):
#     print('books:', book, 'price:', price)
#     print('描述：', desc)
#
#
# my_dict = {'price': 80, 'book': '馒头', 'desc': '熟的'}
# bar(**my_dict)


# def swap(dw):
#     dw['a'], dw['b'] = dw['b'], dw['a']
#     print("在swap()函数里面，a元素的值是:",
#           dw['a'], 'b元素的值是：', dw['b'])
#
#
# dw = {'a': 6, 'b': 9}
# swap(dw)
# print('交换后a元素的值：', dw['a'],
#       '交换后b元素的值：', dw['b'])
#
# print(globals())


def test():
    age = 20
    print(age)
    print(locals()['age'])
    locals()['age'] = 12
    print('xxx', age)
    globals()['x'] = 19
    print(x)


test()
print('\n')
x = 5
y = 20
print(globals())
print(locals())
print(x)
print(globals()['x'])
globals()['x'] = 39
print(x)
locals()['x'] = 99
print(x)

