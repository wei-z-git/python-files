# def foo(fn):
#     def bar(*args):
#         print("===1===", args)
#         n = args[0]
#         print("===2===", n*(n-1))
#         print(fn.__name__)
#         fn(n * (n - 1))
#         print("*" * 15)
#         return fn(n * (n - 1))
#     return bar

# @foo
# def my_test(a):
#     print("===my_test函数===", a)


# print(my_test)
# my_test(10)
# # my_test(6, 5)


# =======================================
def auth(fn):
    print(fn)

    def auth_fn(*args):
        print("======= 模拟执行检查权限 ======")
    #    fn回调参数
        fn(*args)
    # !return auth_fn后，相当于test（）就是auth_fn()了
    return auth_fn


@auth
def test(a, b):
    print("执行test函数，参数a：%s，参数b：%s" % (a, b))


test(20, 15)



# def fn(*args):
#     print(args)


# @fn
# def fn2(a, b):
#     print(a, b)

