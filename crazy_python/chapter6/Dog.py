# class Dog:
#     def jump(self):
#         print("正在执行jump方法")

#     def run(self):
#         self.jump()
#         print('正在执行jump方法')


# class InConstructor:
#     def __init__(self):
#         foo = 0
#         self.foo = 6


# print(InConstructor().foo)
# class User:
#     def test(self):
#         print('self参数', self)


# u = User()
# u.test()

# foo = u.test
# foo()


class ReturnSelf:
    def grow(self):
        if hasattr(self, 'age'):
            # 如果对象object有age属性，则：
            self.age += 1
        else:
            self.age = 1
        return self


rs = ReturnSelf()
rs.grow().grow().grow()
print("rs的age属性值是：", rs.age)