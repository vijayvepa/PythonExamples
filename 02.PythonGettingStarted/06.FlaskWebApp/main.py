from flask import Flask, request, url_for, redirect, render_template

from storage import Storage
from student import Student

app = Flask(__name__)
dictionaries = Storage.load()
students = Student.get_objects(dictionaries)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get('student-id', '')
        new_student_name = request.form.get('name', '')
        new_student_last_name = request.form.get('last-name', '')

        student = Student(f'{new_student_name} {new_student_last_name}', new_student_id)

        students.append(student)
        Storage.save(Student.get_dictionaries(students))

        return redirect(url_for('students_page'))
    if request.method == "DELETE":
        return redirect(url_for('students_page'))
    return render_template('index.html', students=students)

@app.route("/delete", methods=["POST"])
def delete_student():
    delete_student_id = request.form.get('delete-student-id', '')
    Student.delete_by_id(students, delete_student_id)
    Storage.save(Student.get_dictionaries(students))
    return redirect(url_for('students_page'))


if __name__ == "__main__":
    app.run()
