from django.shortcuts import redirect, render
from datetime import datetime
import random

def index(request):
    if not 'game' in request.session:
        request.session['name'] = False
        request.session['gold'] = "N/A"
        request.session['moves'] = "N/A"
        request.session['activities'] = []
        request.session['game'] = True
    if 'scoreboard' not in request.session:
        request.session['scoreboard'] = []
    else:
        request.session['scoreboard'].sort(key=lambda user: user['score'], reverse=True)
    return render(request, 'ninja_gold.html')
def play(request):
    request.session['name'] = request.POST['name']
    request.session['gold'] = 0
    request.session['moves'] = 0
    return redirect('/')
def process_money(request):
    gold = random.randint(int(request.POST['gold-min']), int(request.POST['gold-max']))
    request.session['gold'] += gold
    request.session['moves'] += 1
    outcome = "Earned" if gold > 0 else "Lost"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.POST['facility'] != "casino":
        message = f'{outcome} {gold} golds from the {request.POST["facility"]}! ({current_time})'
    else:
        message = f'Entered a casino and {outcome} {gold} golds.. Ouch.. ({current_time})'
    request.session['activities'].append({'type': outcome, 'message': message})
    if request.session['moves'] == 15:
        request.session['game'] = False
        username = request.session['name']
        user_found = False
        for user in request.session['scoreboard']:
            if user["username"] == username:
                if user['score'] < request.session['gold']:
                    user["score"] = request.session['gold']
                user_found = True
                break
        if user_found == False:
            request.session['scoreboard'].append({"username": username,"score": request.session['gold']})
        request.session['scoreboard'].sort(key=lambda user: user['score'], reverse=True)
    return redirect('/')
def play_again(request):
    session_keys = ['name', 'gold', 'moves', 'activities', 'game']
    for key in session_keys:
        request.session.pop(key, None)
    return redirect('/')
def view_scoreboard(request):
    return render(request,'scoreboard.html')
def clear(request):
    request.session.clear()
    return redirect('/')