# def pow(base, component):
#     result = 1
#     for i in range(1, component + 1):
#         result *= base
#     return result
#
#
# my_fun = pow
# print(my_fun(3, 4))
#
#
# def area(weigh, height):
#     return weigh * height
#
#
#
#


# # 定义fn为传入的一个函数
# def map(data, fn):
#     result = []
#     for e in data:
#         result.append(fn(e))
#     return result
#
#
# def square(n):
#     return n * n
#
#
# def cube(n):
#     return n * n * n
#
#
# data = [3, 4, 5, 6]
# print("原数据：", data)
# c = map(data, square)
# print(c)


# # 就是说math_func 会根据type返回不同的函数
# def get_math_func(type):
#     def square(n):
#         return n * n
#
#     def cube(n):
#         return n * n * n
#
#     def factorial(n):
#         result = 1
#         for index in range(2, n+1):
#             result *= index
#         return result
#
#     if type == "square":
#         return square
#     if type == "cube":
#         return cube
#     else:
#         return factorial
#
#
# math_func = get_math_func("cube")
# print(math_func(5))


def get_math_func(type):
    # def square(n):
    #     return n*n
    #
    # def cube(n):
    #     return n*n*n
    #
    # def factorial(n):
    #     result = 1
    #     for i in range(0, n):
    #         result *= i

    if type == "square":
        return lambda n: n * n
    elif type == "cube":
        return lambda n: n * n * n
    else:
        return lambda n: (1+n) * n/2


a = get_math_func("square")

a = get_math_func("square")
print(a(44))
