from django.shortcuts import render, redirect
from users_app.models import User

def index(request):
    request.session['users'] = list(User.objects.all().values('id', 'first_name', 'last_name', 'email_address', 'age'))
    return render(request, 'index.html')
def add_user(request):
    if len(request.POST['first_name']) < 1 or len(request.POST['last_name']) < 1 or len(request.POST['email_address']) < 1 or len(request.POST['age']) < 1:
        return redirect('/')
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], age=request.POST['age'])
    return redirect('/')