from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
def login(request):
    errors = User.objects.login_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='login')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['first_name'] = user.first_name
    request.session['last_name'] = user.last_name
    return redirect('/success')
def register(request):
    errors = User.objects.registration_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/')
    User.objects.create_user(request.POST)
    messages.success(request, "Registration successful! You can now log in.", extra_tags='success')
    return redirect('/')
def success(request):
    if not 'first_name' in request.session:
        messages.error(request, 'You must first login.', extra_tags='login')
        return redirect('/')
    return render(request,'success.html')
def logout(request):
    request.session.clear()
    return redirect('/')