from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'very secret key'

@app.route('/')
def render_main_page():
    if not 'random_num' in session:
        session['random_num'] = random.randint(1, 100)
        session['attempts'] = 0
        session['result'] = False
        session['lost'] = False
    if not 'users' in session:
        session['users'] = []
    else:
        session['users'].sort(key=lambda user: user['score'])
    return render_template("great_number_game.html", result=session['result'], attempts=session['attempts'], guess=session['random_num'], lost=session['lost'], users=session['users'])
@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) == session['random_num']:
        session['result'] = True
    elif int(request.form['guess']) > session['random_num']:
        session['result'] = 'Too High!'
        session['attempts'] += 1
        if session['attempts'] == 10:
            session['lost'] = True
    elif int(request.form['guess']) < session['random_num']:
        session['result'] = 'Too Low!'
        session['attempts'] += 1
        if session['attempts'] >= 10:
            session['lost'] = True
    return redirect('/')
@app.route('/play_again', methods=['POST'])
def play_again():
    session_keys = ['random_num', 'attempts', 'result', 'lost']
    username = request.form.get('user_name')
    if username == None:
        for key in session_keys:
            session.pop(key, None)
        return redirect('/')
    user_found = False
    for user in session['users']:
        if user["username"] == request.form['user_name']:
            if user['score'] > session['attempts']:
                user["score"] = session['attempts']
            user_found = True
            break
    if user_found == False:
        session['users'].append({"username": request.form['user_name'],"score": session['attempts']})
    for key in session_keys:
        session.pop(key, None)
    return redirect('/')
@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)