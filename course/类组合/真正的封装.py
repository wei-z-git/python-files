class People:
    def __init__(self, name, age):
        self.set_info(name, age)

    def tell_info(self):
        print('姓名：<%s> 年龄<%s>' % (self.name, self.age))

    def set_info(self, name, age):
        if type(name) is not str:
            raise TypeError('name must be str!')
        if type(age) is not int:
            raise TypeError('age must be int!')

        self.__name = name
        self.__age = age


p = People('馒头', 18)
# p.tell_info()
p.set_info(123.1, 123)
