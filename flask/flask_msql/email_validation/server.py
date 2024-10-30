from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'very secret key'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def render_main_page():
    return render_template("index.html")
@app.route('/success', methods=['POST'])
def display_result():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
        return redirect("/")
    else:
        mysql = connectToMySQL("emails")
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        data = {
            "email": request.form['email']
        }
        email = mysql.query_db(query, data)
        if email:
            flash("Email is already entered!")
            return redirect("/")
        else:
            mysql = connectToMySQL("emails")
            query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW())"
            data = {
                "email": request.form["email"]
            }
            mysql.query_db(query, data)
            flash(f"The email address you entered ({request.form['email']}) is a VALID email address! Thank you!")
            mysql2 = connectToMySQL("emails")
            emails = mysql2.query_db("SELECT * FROM emails;")
            return render_template("success.html", emails=emails)
@app.route('/delete_email/<email>', methods=['GET'])
def delete_email(email):
    mysql = connectToMySQL("emails")
    query = "DELETE FROM emails WHERE email = %(email)s"
    data = {
        "email": email,
    }
    mysql.query_db(query, data)
    flash(f"Email ({email}) was successfully deleted.")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)