from student import Student

class Alumnus(Student):
    def __init__(self, graduation_year, name):
        super().__init__(name)
        self.graduation_year = graduation_year

    def __str__(self):
        studentstr = super().__str__().replace("\n","")
        return f'Alumnus{{ student: {studentstr}, graduated: {self.graduation_year} }}\n'