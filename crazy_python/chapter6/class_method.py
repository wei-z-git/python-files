# class Bird:
#     @classmethod
#     def fly(cls):
#         print('类方法：', cls)
#     @staticmethod
#     def info(p):
#         print('静态方法：', p)


# Bird.fly()
# Bird.info('infop')

def functionA(fn):
    print('A')
    fn()
    return 'fxit'


@functionA
def functionB():
    print('B')


print(functionB)
