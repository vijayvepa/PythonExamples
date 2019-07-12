def print_student_markup(list_name, list):
    print(f'\n## {list_name}')
    for student in list:
        print(f'- {student}')


student_list = []
i = 0
while len(student_list) < 10:
    i = i + 1
    student_list.append(f'Student number {i}')
    print(student_list)


print_student_markup('Student List', student_list)
alt_student_list = []

for index in range(22, 41, 3):
    alt_student_list.append(f'Alt Student number {index}')

print_student_markup('Alt Student List', alt_student_list)

for student in student_list:
    if student == 'Student number 4':
        print('found student 4')
        break
    else:
        print('looking for student 4')

for student in student_list:
    print('looking for student 4 with continue...')
    if student != 'Student number 4':
        continue

    print('processing 4')

while True:
    print('forever loop, control c to exit')
