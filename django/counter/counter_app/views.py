from django.shortcuts import redirect, render
from django.shortcuts import redirect, render

def root(request):
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 0
    if not 'counter' in request.session:
        request.session['counter'] = 0
    return render(request, 'counter.html')
def destroy_session(request):
    request.session.clear()
    return redirect("/")
def handle_action(request):
    if request.POST['action'] == 'add2':
        request.session['counter'] += 2
    elif request.POST['action'] == 'reset':
        request.session.pop('counter')
    return redirect("/")
def custom_increment(request):
    request.session['counter'] += (int(request.POST['increments']))
    return redirect("/")