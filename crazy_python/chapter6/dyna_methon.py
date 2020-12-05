# class Cat:
#     def __init__(self, name):
#         self.name = name

# def walk_func(self):
#         print('%s慢慢走过一片草地' % self.name)


# d1 = Cat('xiaoming')
# d2 = Cat('xiaohong')
# Cat.walk = walk_func
# d1.walk()
# d2.walk()


class Dog:
    __slots__ = ('walk', "age", "name")
    def __init__(self, name):
        self.name = name
    def test():
        print('预先定义的test方法')


def haha(self):
    print('my name is %s' % self.name)

Dog.haha = haha
d = Dog('xiaowang')
from types import MethodType

# d.foo = 50

d.haha()