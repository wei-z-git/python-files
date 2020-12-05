# def foo():
#     print("全局空间的foo方法")
# bar = 20


# class Bird:
#     def foo():
#         print("Bird空间的foo方法")
#     bar = 200


# foo()
# print(bar)

# Bird.foo()
# print(Bird.bar)

class User:
    def walk(self):
        print(self, '正在慢慢走')


# 创建一个对象u
u = User()
# 对象u调用方法walk
u.walk()
# 类调用方法walk
User.walk(u)
