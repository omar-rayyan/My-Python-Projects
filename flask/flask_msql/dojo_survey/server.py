from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'very secret key'

@app.route('/')
def render_main_page():
    return render_template("dojo_survey.html")
@app.route('/result', methods=['POST'])
def display_result():
    likes_mansaf = 'Yes' if 'likesMansaf' in request.form else 'No'
    is_valid = True
    if len(request.form["name"]) < 1:
        is_valid = False
        flash("Please enter a name")
    if len(request.form["gender"]) < 1:
        is_valid = False
        flash("Please choose a gender")
    if not is_valid:
        return redirect("/")
    else:
        mysql = connectToMySQL("surveys")
        query = "INSERT INTO surveys (name, location, favorite_language, gender, likes_mansaf, comment, created_at) VALUES (%(name)s, %(location)s, %(favorite_language)s, %(gender)s, %(likes_mansaf)s, %(comment)s, NOW())"
        data = {
            "name": request.form["name"],
            "location": request.form["location"],
            "favorite_language": request.form["favoriteLanguage"],
            "gender": request.form["gender"],
            "likes_mansaf": 1 if likes_mansaf == "Yes" else 0,
            "comment": request.form["comment"],
        }
        mysql.query_db(query, data)
        flash("Survey successfully registered!")
        return render_template("result.html", name=request.form['name'], location=request.form['location'],
        favorite_language=request.form['favoriteLanguage'], gender=request.form.get('gender'), likesMansaf=likes_mansaf,
        comment=request.form['comment'])
@app.route('/go_back', methods=['POST'])
def go_back():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)