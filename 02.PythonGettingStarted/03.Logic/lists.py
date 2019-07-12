student_list = ['mark', 'katrina', 'angelo']

mark_is_first_student = student_list[0] == "mark"
mark_is_also_third_from_last = student_list[-3] == "mark"

print(mark_is_first_student)
print(mark_is_also_third_from_last)

student_list[0] = 'james'

james_is_now_first_student = student_list[0] == "james"

print(james_is_now_first_student)

if "mark" not in student_list:
    student_list.append('mark')
    print(student_list)
    print(student_list.__len__())
else:
    print('mark already in student list')


if len(student_list) < 4:
    print('student list less than 4')
else:
    print('student list >= 4')

print(f'Sliced student list {student_list[1:3]}')
print(f'Left sliced student list {student_list[1:]}')

index =  student_list.index('katrina', 0, 5)
print(f'katrina is at  {index}')

#del student_list[1]

student_list.remove('katrina')

if "katrina" in student_list:
    print('katrina still in student list')
else:
    print('katrina not in student_list anymore')