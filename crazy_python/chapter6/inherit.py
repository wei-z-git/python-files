# class Fruit:
#     def info(self):
#         print("我是一个水果！重%g克" % self.weight)


# class Food:
#     def taste(self):
#         print("不同食物的口感不同")


# class Apple(Fruit, Food):  #多继承，不推荐使用
#     pass


# a = Apple()
# a.weight = 5.6
# a.info()
# a.taste()

# 子类重写父类
class Bird:
    def fly(self):
        print("我在天空翱翔")


class Ostrich(Bird):
    def fly(self):
        print("我只能在地上走")


os = Ostrich()
os.fly()
