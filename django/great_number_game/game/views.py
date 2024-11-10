from django.shortcuts import redirect, render
import random
from game.models import User

def index(request):
    if not 'random_num' in request.session:
        request.session['random_num'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['result'] = False
        request.session['lost'] = False
    update_scoreboard(request)
    return render(request, 'great_number_game.html')
def guess(request):
    if len(request.POST['guess']) < 1:
        return redirect('/')
    if int(request.POST['guess']) == request.session['random_num']:
        request.session['result'] = True
    elif int(request.POST['guess']) > request.session['random_num']:
        difference = int(request.POST['guess']) - request.session['random_num']
        if difference >= 20:
            request.session['result'] = 'Too High!'
        elif difference <= 5:
            request.session['result'] = 'A Little High!'
        elif difference <= 15:
            request.session['result'] = 'High!'
        request.session['attempts'] += 1
        if request.session['attempts'] == 10:
            request.session['lost'] = True
    elif int(request.POST['guess']) < request.session['random_num']:
        difference = request.session['random_num'] - int(request.POST['guess'])
        if difference >= 20:
            request.session['result'] = 'Too Low!'
        elif difference <= 5:
            request.session['result'] = 'A Little Low!'
        elif difference <= 15:
            request.session['result'] = 'Low!'
        request.session['attempts'] += 1
        if request.session['attempts'] >= 10:
            request.session['lost'] = True
    return redirect('/')
def play_again(request):
    session_keys = ['random_num', 'attempts', 'result', 'lost']
    username = request.POST.get('user_name')
    if username == None:
        for key in session_keys:
            request.session.pop(key, None)
        return redirect('/')
    User.objects.create_user(username, int(request.session['attempts']))
    for key in session_keys:
        request.session.pop(key, None)
    return redirect('/')
def clear(request):
    request.session.clear()
    return redirect('/')

def update_scoreboard(request):
    request.session['scoreboard'] = []
    users = User.objects.all()
    for user in users:
        request.session['scoreboard'].append({'username': user.username, 'score': user.score})
    request.session['scoreboard'].sort(key=lambda user: user['score'])