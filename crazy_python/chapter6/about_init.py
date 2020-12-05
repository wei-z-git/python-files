# _init_的作用可能是为了将隐形的变量显形吧

# 注意1、__init__并不相当于C#中的构造函数，执行它的时候，实例已构造出来了。

# class A(object):
#     def __init__(self,name):
#         self.name=name
#     def getName(self):
#         return 'A '+self.name
 

# 当我们执行

# a=A('hello')
# 时，可以理解为
# a=object.__new__(A)
# A.__init__(a,'hello')
 

# 即__init__作用是初始化已实例化后的对象。



class Rectangle:
  def area(self):
    return self.length * self.width


tr = Rectangle()
tr.length, tr.width = 1, 2
print(tr.area())
