# def get_math_func(type, nn):
#     def square(n):
#         return n*n
#     def cube(n):
#         return n*n*n
#     def factorial(n):
#         result = 1
#         for index in range(2, n+1):
#             result *= index
#         return result
#     if type == "square":
#         return square(nn)
#     elif type == 'cobe':
#         return cube(nn)
#     else:
#         return factorial(nn)
#
#
# print(get_math_func('square', 3))


def foo():
    name = 'cat'

    def bar():
        print(name)
        # name = 'hahah'
    bar()


foo()