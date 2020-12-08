class People:
    def __init__(self, name, age, height, weight):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight

    def bmi(self):
        return self.__weight / (self.__height ** 2)

egon=People('egon',18,1.80,75)
print(egon.bmi())





# rect = Rectangle(4, 3)
# print(rect.width)
# rect.size = 9, 7
# print(rect.width)

# rect.delSize()
# print(rect.width)

# class User :
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#     def getfullname(self):
#         return self.first + ',' +self.last
#     def setfullname(self, fullname):
#         first_last = fullname.rsplit(',')
#         self.first = first_last[0]
#         self.last = first_last[1]
#     fullname = property(getfullname, setfullname)

# u = User("悟空", "孙")
# print(u.fullname)
# u.fullname = "八戒,煮"
# print(u.first)

# class Cell:
#     @property
#     def state(self):
#         return self._state
#     @state.setter
#     def state(self, value):
#         if 'alive' in value.lower():
#             self._state = 'alive'
#         else:
#             self._state = 'dead'
#     @property
#     def is_dead(self):
#         return not self._state.lower() == 'alive'


# c = Cell()
# c.state = 'ALive'
# print(c.state)
# print(c.is_dead)
