class Student():

    def __init__(self, name, age, *score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(max(self.score))


zm = Student('zhangming', 20, [69, 88, 100])
Cyg = Student('CaoYougen', 21, [80, 100, 30])
print(' 学生姓名为: ', zm.get_name(), '\n', '学生年龄为：', zm.get_age(), '\n',
      '3门科目中最高分数为:', zm.get_course())
print()
print(' 学生姓名为: ', Cyg.get_name(), '\n', '学生年龄为：', Cyg.get_age(), '\n',
      '3门科目中最高分数为:', Cyg.get_course())
