student = {"name": "Mark", "id": 12345, "feedback": None}
all_students = [
    student,
    {"name": "Jessica", "id": 12346, "feedback": "Good", "last_name": "Simpson"},
    {"name": "Andrew", "id": 12347, "feedback": "Okay"}
]

print(student['name'])

print('last names:')
for s in all_students:
    print(f'- {s.get("last_name", None)}')

try:
    number_add = 3 + all_students[1]['last_name']
    print(student['last_name'])


except Exception as error:
    print('Exception handled: {0}'.format(error))