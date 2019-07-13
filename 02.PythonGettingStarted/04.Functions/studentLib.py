import json


def load_students():
    try:
        with open('resources/students.json', 'r') as f:
            return json.load(f)
    except Exception as ex:
        print(f'Error loading students {ex}')
        return []


students = load_students()


def get_students_titlecase():
    students_title_case = []
    for student in students:
        students_title_case.append(f"{student['name'].title()}({student['id']})")
    return students_title_case


def print_students_titlecase():
    students_title_case = get_students_titlecase()
    print(students_title_case)


def add_student(name, student_id=None):
    students.append({'name': name, 'id': student_id})


def add_student_kw(**kwargs):
    students.append(kwargs)


def var_args(name, *args):
    print(name)
    print(args)


def keyword_args(name, **kwargs):
    print(name)
    print(kwargs)


def save_students():
    try:
        f = open('resources/students.json', 'w')
        json.dump(students, f)
        f.close()
    except Exception as error:
        print(f'Error saving file : {error}')


add_student(name='mark', student_id=5)
add_student('JULIE')
print_students_titlecase()
var_args('test', '1', 2, 3)
keyword_args('test', description='hello', ascii='ascii')
add_student_kw(name='matt', id=5)
print_students_titlecase()
save_students()
