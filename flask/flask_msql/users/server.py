from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')
@app.route('/users')
def display_users():
    mysql = connectToMySQL("users")
    users = mysql.query_db("SELECT * FROM users;")
    return render_template("users.html", users=users)
@app.route('/add_user', methods=["GET"])
def add_user_page():
    return render_template("new_user.html")
@app.route("/add_user", methods=["POST"])
def add_user():
    mysql = connectToMySQL("users")
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())"
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    user_id = mysql.query_db(query, data)
    return redirect(f'/show_user/{user_id}')
@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    mysql = connectToMySQL("users")
    query = "DELETE FROM users WHERE user_id = %(user_id)s"
    data = {
        "user_id": user_id,
    }
    mysql.query_db(query, data)
    return redirect('/users')
@app.route('/show_user/<int:user_id>')
def show_user(user_id):
    mysql = connectToMySQL("users")
    query = "SELECT * FROM users WHERE user_id = %(user_id)s;"
    data = {
        "user_id": user_id
    }
    user = mysql.query_db(query, data)
    if user:
        return render_template("show_user.html", user=user[0])
    else:
        return redirect('/users')
@app.route('/edit_user/<int:user_id>', methods=['GET'])
def edit_user_page(user_id):
    mysql = connectToMySQL("users")
    query = "SELECT * FROM users WHERE user_id = %(user_id)s;"
    data = {
        "user_id": user_id
    }
    user = mysql.query_db(query, data)
    return render_template("edit_user.html", user=user[0])
@app.route("/edit_user_finish", methods=["POST"])
def edit_user():
    mysql = connectToMySQL("users")
    query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE user_id = %(user_id)s"
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "user_id": request.form["user-id"],
    }
    mysql.query_db(query, data)
    return redirect(f'/show_user/{request.form["user-id"]}')
if __name__ == "__main__":
    app.run(debug=True)