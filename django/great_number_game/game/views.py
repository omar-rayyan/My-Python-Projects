from django.shortcuts import redirect, render
import random

def index(request):
    if not 'random_num' in request.session:
        request.session['random_num'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['result'] = False
        request.session['lost'] = False
    if not 'users' in request.session:
        request.session['users'] = []
    else:
        request.session['users'].sort(key=lambda user: user['score'])
    return render(request, 'great_number_game.html')
def guess(request):
    if len(request.POST['guess']) < 1:
        return redirect('/')
    if int(request.POST['guess']) == request.session['random_num']:
        request.session['result'] = True
    elif int(request.POST['guess']) > request.session['random_num']:
        request.session['result'] = 'Too High!'
        request.session['attempts'] += 1
        if request.session['attempts'] == 10:
            request.session['lost'] = True
    elif int(request.POST['guess']) < request.session['random_num']:
        request.session['result'] = 'Too Low!'
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
    user_found = False
    for user in request.session['users']:
        if user["username"] == request.POST['user_name']:
            if user['score'] > request.session['attempts']:
                user["score"] = request.session['attempts']
            user_found = True
            break
    if user_found == False:
        request.session['users'].append({"username": request.POST['user_name'],"score": request.session['attempts']})
    for key in session_keys:
        request.session.pop(key, None)
    return redirect('/')
def clear(request):
    request.session.clear()
    return redirect('/')