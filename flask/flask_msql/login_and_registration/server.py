from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt   

app = Flask(__name__)
app.secret_key = 'very secret key'

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d).+$')

@app.route('/')
def render_main_page():
    return render_template("index.html")
@app.route('/register', methods=['POST'])
def register():
    is_valid = True
    if len(request.form['first_name']) < 1:
        is_valid = False
        flash("Please provide a first name.", "register")
        return redirect("/")
    if len(request.form['last_name']) < 1:
        is_valid = False
        flash("Please provide a last name.", "register")
        return redirect("/")
    if len(request.form['email']) < 1:
        is_valid = False
        flash("Please provide an email address.", "register")
        return redirect("/")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("The email address you've entered is invalid.", "register")
        return redirect("/")
    if len(request.form['password']) < 1:
        is_valid = False
        flash("Please provide a password.", "register")
        return redirect("/")
    if not PASSWORD_REGEX.match(request.form['password']):
        is_valid = False
        flash("Password must contain at least one uppercase letter and one number.", "register")
    if request.form['password'] != request.form['password-confirmation']:
        is_valid = False
        flash("Passwords do not match.", "register")
        return redirect("/")
    if not is_valid:
        return redirect("/")
    else:
        mysql = connectToMySQL("users")
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {
            "email": request.form['email']
        }
        email = mysql.query_db(query, data)
        if email:
            flash("This email has previously been used. Please login to your account.", "register")
            return redirect("/")
        else:
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
            mysql = connectToMySQL("users")
            query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
            data = {
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"],
                "password": pw_hash
            }
            mysql.query_db(query, data)
            session['first_name'] = request.form['first_name']
            session['last_name'] = request.form['last_name']
            return redirect("/success")
@app.route('/login', methods=['POST'])
def login():
    is_valid = True
    if len(request.form['email']) < 1:
        is_valid = False
        flash("Please provide an email address.", "login")
        return redirect("/")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("The email address you've entered is invalid.", "login")
        return redirect("/")
    if len(request.form['password']) < 1:
        is_valid = False
        flash("Please provide a password.", "login")
        return redirect("/")
    if not is_valid:
        return redirect("/")
    else:
        mysql = connectToMySQL("users")
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {
            "email": request.form['email']
        }
        user = mysql.query_db(query, data)
        if user:
            if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
                session['first_name'] = user[0]['first_name']
                session['last_name'] = user[0]['last_name']
                return redirect("/success")
            else:
                flash("Incorrect password.", "login")
                return redirect("/")
        else:
            flash("Email not found", "login")
            return redirect("/")
@app.route('/success')
def success_page():
    return render_template("success.html", first_name=session['first_name'])
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)