from flask import Flask, render_template, request, redirect, session # type: ignore
from datetime import datetime

import random

app = Flask(__name__)
app.secret_key = 'very secret key'

@app.route('/')
def render_main_page():
    if not 'game' in session:
        session['name'] = False
        session['gold'] = "N/A"
        session['moves'] = "N/A"
        session['activities'] = []
        session['game'] = True
    if not 'scoreboard' in session:
        session['scoreboard'] = []
    else:
        session['scoreboard'].sort(key=lambda user: user['score'], reverse=True)
    return render_template("ninja_gold.html", name=session['name'], gold=session['gold'], activities=session['activities'], moves=session['moves'], game=session['game'])
@app.route('/play', methods=['POST'])
def play():
    session['name'] = request.form['name']
    session['gold'] = 0
    session['moves'] = 0
    return redirect('/')
@app.route('/process_money', methods=['POST'])
def process_money():
    gold = random.randint(int(request.form['gold-min']), int(request.form['gold-max']))
    session['gold'] += gold
    session['moves'] += 1
    outcome = "Earned" if gold > 0 else "Lost"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.form['facility'] != "casino":
        message = f'{outcome} {gold} golds from the {request.form["facility"]}! ({current_time})'
    else:
        message = f'Entered a casino and {outcome} {gold} golds.. Ouch.. ({current_time})'
    session['activities'].append({'type': outcome, 'message': message})
    if session['moves'] == 15:
        session['game'] = False
        username = session['name']
        user_found = False
        for user in session['scoreboard']:
            if user["username"] == username:
                if user['score'] < session['gold']:
                    user["score"] = session['gold']
                user_found = True
                break
        if user_found == False:
            session['scoreboard'].append({"username": username,"score": session['gold']})
        session['scoreboard'].sort(key=lambda user: user['score'], reverse=True)
    return redirect('/')
@app.route('/play_again', methods=['POST'])
def play_again():
    session_keys = ['name', 'gold', 'moves', 'activities', 'game']
    for key in session_keys:
        session.pop(key, None)
    return redirect('/')
@app.route('/view_scoreboard')
def view_scoreboard():
    return render_template('scoreboard.html', scoreboard=session['scoreboard'])
@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)