class Student:
    school_name = 'Roch Memorial High'

    def __init__(self, name, student_id=None):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f'Student{{ school: {Student.school_name}, name: {self.get_name_title_case()}, id: {self.student_id} }} \n'

    def get_name_title_case(self):
        """
        gets the name of the student with title case
        :return: name with title case
        """
        return self.name.title()

    def set_id(self, student_id):
        self.student_id = student_id

    def __repr__(self):
        return self.__str__()






