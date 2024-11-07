from django.shortcuts import render, redirect
from users.models import User
from django.contrib import messages

def root(request):
    if not 'user_id' in request.session:
        return render(request, 'index.html')
    else:
        return redirect('/books')
def login(request):
    errors = User.objects.login_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='login')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['first_name'] = user.first_name
    request.session['last_name'] = user.last_name
    request.session['user_id'] = user.id
    return redirect('/books')
def register(request):
    errors = User.objects.registration_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/')
    User.objects.create_user(request.POST)
    messages.success(request, "Registration successful! You can now log in.", extra_tags='success')
    print('ummmm')
    return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')