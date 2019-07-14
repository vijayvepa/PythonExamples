from student import Student
from alumnus import Alumnus

students = []

student1 = Student('aMarnath')
student2 = Student('aJaY', 2)
student1.set_id(45)
alumnus1 = Alumnus(1997, 'vijay')
alumnus1.set_id(55)

students.append(student1)
students.append(student2)
students.append(alumnus1)

print(students)