class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('<名字：%s 年龄: %s 性别: %s>' % (self.name, self.age, self.sex))


class OldboyStudent(OldboyPeople):
    def __init__(self, name, age, sex, course, stu_id):
        OldboyPeople.__init__(self, name, age, sex)
        self.course = course
        self.stu_id = stu_id

    def learn(self):
        print('%s is learning' % self.name)


class OldboyTeacher(OldboyPeople):
    def __init__(self, name, age, sex, level, salary):
        OldboyPeople.__init__(self, name, age, sex)
        self.level = level
        self.salary = salary

    def learn(self):
        print('%s is teacher' % self.name)


class Data:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tell_birth(self):
        print('出生日期是：<%s-%s-%s>' % (self.year, self.month, self.day))


stu1 = OldboyStudent('馒头', 18, 'female', 'math', 108)
data_obj1 = Data(2002, 5, 18)
stu1.birth = data_obj1

teacher1 = OldboyTeacher('花卷', 40, 'male', 10, 3000)
data_obj2 = Data(1970, 1, 1)
teacher1.birth = data_obj2
stu1.birth.tell_birth()

# stu1.learn()
