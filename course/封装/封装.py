# 封装
class People:
    def __init__(self, name, age):
        # self.__name = name
        # self.__age = age
        self.set_info(name, age)

    def tell_info(self):
        print("name:<%s> age:<%s>" % (self.__name, self.__age))

    def set_info(self, name, age):
        self.__name = name
        self.__age = age
