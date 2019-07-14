class Student:
    school_name = 'Roch Memorial High'

    def __init__(self, firstname, lastname, student_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id

    def __str__(self):
        return f'Student{{ school: {Student.school_name}, name: {self.get_name_title_case()}, id: {self.student_id} }} \n'

    def get_name_title_case(self):
        """
        gets the name of the student with title case
        :return: name with title case
        """
        return self.firstname.title()

    def set_id(self, student_id):
        self.student_id = student_id

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def get_dictionaries(students):
        dictionaries = []
        for student in students:
            dictionaries.append(
                {'firstname': student.firstname, 'lastname': student.lastname, 'id': student.student_id})
        return dictionaries

    @staticmethod
    def get_objects(dictionaries):
        students = []
        for dictionary in dictionaries:
            students.append(
                Student(dictionary.get('firstname', ''), dictionary.get('lastname', ''), dictionary.get('id', '')))
        return students

    @staticmethod
    def delete_by_id(students: list, student_id: str):
        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                del student
                break
