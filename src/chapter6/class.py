class Person:
    def __init__(self, name='charlie', age=9):
        self.name = name
        self.age = age

    def say(self, content):
        print(content)


p = Person()

p.say("papa")
