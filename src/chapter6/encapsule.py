class User:
    def __hide(self):
        print('示范隐藏方法')

    def getname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名必须在3-8之间')
        self.__name = name
    name = property(getname, setname)

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户年龄在18-70！')
        self.__age = age

    def getage(self):
        return self.__age
    age = property(getage, setage)


u = User()

u.name = "asdasdadasdadasd"

