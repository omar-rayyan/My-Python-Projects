from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'very secret key'

@app.route('/')
def render_main_page():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0
    if not 'counter' in session:
        session['counter'] = 0
    return render_template("counter.html", visits=session['visits'], counter=session['counter'])
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")
@app.route('/handle_action', methods=['POST'])
def add2():
    if request.form['action'] == 'add2':
        session['counter'] += 2
    elif request.form['action'] == 'reset':
        session.pop('counter')
    return redirect("/")
@app.route('/custom_increment', methods=['POST'])
def custom_increment():
    session['counter'] += (int(request.form['increments']))
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)