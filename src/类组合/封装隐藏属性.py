class Foo:
    def __f1(self):
        print('Foo.f1')

    def f2(self):
        print('Fpp.f2')
        self.__f1()


class Bar(Foo):
    def __f1(self):
        print('Bar.f1')


b = Bar()
b.f2()
