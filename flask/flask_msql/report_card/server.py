from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = 'very secret key'

@app.route('/')
def display_students():
    mysql = connectToMySQL("report_card")
    students = mysql.query_db("SELECT * FROM students;")
    return render_template("index.html", students=students)
@app.route('/add_student', methods=["GET"])
def add_student_page():
    return render_template("add_student.html")
@app.route("/add_student", methods=["POST"])
def add_student():
    if len(request.form['first_name']) < 1:
        flash("Please provide a first name.")
        return redirect("/add_student")
    if len(request.form['last_name']) < 1:
        flash("Please provide a last name.")
        return redirect("/add_student")
    if len(request.form['year']) < 1:
        flash("Please provide a year.")
        return redirect("/add_student")
    mysql = connectToMySQL("report_card")
    query = "INSERT INTO students (first_name, last_name, year, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(year)s, NOW(), NOW())"
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "year": request.form["year"]
    }
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/add_grade/<int:student_id>', methods=['GET'])
def add_grade_page(student_id):
    session['student_id'] = student_id
    return render_template("add_grade.html", student_id=student_id)
@app.route("/add_grade", methods=["POST"])
def add_grade():
    if len(request.form['course']) < 1:
        flash("Please provide a course name.")
        return add_grade_page(session['student_id'])
    if len(request.form['grade']) < 1:
        flash("Please provide a grade.")
        return add_grade_page(session['student_id'])
    if len(request.form['comments']) < 1:
        flash("Please provide a comment.")
        return add_grade_page(session['student_id'])
    mysql = connectToMySQL("report_card")
    query = "INSERT INTO grades (student_id, course, grade, comments, date_graded, created_at, updated_at) VALUES (%(student_id)s, %(course)s, %(grade)s, %(comments)s, %(date_graded)s, NOW(), NOW())"
    data = {
        "student_id": session["student_id"],
        "course": request.form["course"],
        "grade": request.form["grade"],
        "comments": request.form["comments"],
        "date_graded": request.form["date_graded"]
    }
    mysql.query_db(query, data)
    return display_report_card(session['student_id'])
@app.route('/delete_student/<int:student_id>', methods=['GET'])
def delete_student(student_id):
    mysql = connectToMySQL("report_card")
    query = "DELETE FROM students WHERE student_id = %(student_id)s"
    data = {
        "student_id": student_id,
    }
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/display_report_card/<int:student_id>', methods=['GET'])
def display_report_card(student_id):
    mysql = connectToMySQL("report_card")
    query = "SELECT * FROM grades JOIN students ON students.student_id = grades.student_id WHERE students.student_id = %(student_id)s ORDER BY FIELD(grade, 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F');"
    data = {
        "student_id": student_id
    }
    grades = mysql.query_db(query, data)
    mysql = connectToMySQL("report_card")
    query_student_info = "SELECT * FROM students WHERE student_id = %(student_id)s;"
    data_student_info = {
        "student_id": student_id
    }
    student_info = mysql.query_db(query_student_info, data_student_info)
    student = student_info[0]
    session['student_id'] = student['student_id']
    session['first_name'] = student['student_id']
    return render_template("report_card.html", grades=grades, student_info=student_info)
@app.route('/delete_grade/<int:grade_id>', methods=['GET'])
def delete_grade(grade_id):
    mysql = connectToMySQL("report_card")
    query = "DELETE FROM grades WHERE grade_id = %(grade_id)s"
    data = {
        "grade_id": grade_id,
    }
    mysql.query_db(query, data)
    return display_report_card(session['student_id'])
@app.route('/edit_grade/<int:grade_id>', methods=['GET'])
def edit_grade_page(grade_id):
    mysql = connectToMySQL("report_card")
    query_grade_info = "SELECT * FROM grades WHERE grade_id = %(grade_id)s;"
    data_grade_info = {
        "grade_id": grade_id
    }
    grade_info = mysql.query_db(query_grade_info, data_grade_info)
    grade = grade_info[0]
    session['grade_id'] = grade['grade_id']
    session['course'] = grade['course']
    session['date_graded'] = grade['date_graded']
    session['comments'] = grade['comments']
    return render_template("edit_grade.html", course=session['course'], date_graded=session['date_graded'], comments=session['comments'], student_id=session['student_id'])
@app.route("/edit_grade", methods=["POST"])
def edit_grade():
    if len(request.form['course']) < 1:
        flash("Please provide a course name.")
        return edit_grade_page(session['grade_id'])
    if len(request.form['grade']) < 1:
        flash("Please provide a grade.")
        return edit_grade_page(session['grade_id'])
    if len(request.form['comments']) < 1:
        flash("Please provide a comment.")
        return edit_grade_page(session['grade_id'])
    mysql = connectToMySQL("report_card")
    query = "UPDATE grades SET course = %(course)s, grade = %(grade)s, comments = %(comments)s, date_graded = %(date_graded)s, updated_at = NOW() WHERE grade_id = %(grade_id)s"
    data = {
        "course": request.form["course"],
        "grade": request.form["grade"],
        "comments": request.form["comments"],
        "date_graded": request.form["date_graded"],
        "grade_id": session["grade_id"],
    }
    mysql.query_db(query, data)
    return display_report_card(session['student_id'])
if __name__=="__main__":
    app.run(debug=True)
