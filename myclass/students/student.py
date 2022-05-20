student = []


class Student:

    def __init__(self, name: str, age: int, ID: str, Class: str, grade: float):
        self.name = name
        self.age = age
        self.ID = ID
        self.Class = Class
        self.grade = grade

    def display(self):
        print(
            'name:',
            self.name,
            '\nage:',
            self.age,
            '\nStudentID:',
            self.ID,
            '\nClass:',
            self.Class,
            '\ngrade:',
            self.grade,
        )

    def alldisplay(list):
        for i in list:
            i.display()
            print('--------------------------------')
