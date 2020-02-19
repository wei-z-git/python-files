from types import MethodType


class Person:
    # _init_构造方法，有了这个就不需要 p = new person()了，？
    def __init__(self, name="tom", age=9):
        name = name
        age = age

    def say(self, content):
        print(content)


p = Person()


def intro_func(self, content):
    print("添加了一个函数 %s" % content)


p.intro = MethodType(intro_func, p)
# 用methodtype将p.intro函数的第一个参数，绑定为p

p.intro("haha")
# 这时候就需要传入自己本身实例p了 而且self因为不是类内部定义的，所以不能p.add(self, "haha")



# def info(self,):
#     print("hahaha")


# p.haha = info




# p = Person("tom222")

# # p.say("papa")
# # print(p.name)
# p.skills = ["swiming", "sging"]
# # print(p.skills)
# # del p.name


# def info(self, content):
#     print("---info函数---", self)


# # p.foo = info
# # p.foo(p)
# p.info = MethodType(info_func, p)
# p.info()
