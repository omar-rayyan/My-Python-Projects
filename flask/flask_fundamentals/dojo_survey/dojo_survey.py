from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'very secret key'

@app.route('/')
def render_main_page():
    return render_template("dojo_survey.html")
@app.route('/result', methods=['POST'])
def display_result():
    likes_mansaf = 'Yes' if 'likesMansaf' in request.form else 'No'
    return render_template("result.html", name=request.form['name'], location=request.form['location'],
    favorite_language=request.form['favoriteLanguage'], gender=request.form.get('gender'), likesMansaf=likes_mansaf,
    comment=request.form['comment'])
@app.route('/go_back', methods=['POST'])
def go_back():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)