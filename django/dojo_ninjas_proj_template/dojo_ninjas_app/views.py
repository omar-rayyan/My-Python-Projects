from django.shortcuts import render,redirect
from dojo_ninjas_app.models import Dojo, Ninja

def index(request):
    dojos = Dojo.objects.all()
    for dojo in dojos:
        dojo.ninjas_list = dojo.ninjas.all().values('first_name', 'last_name')
    return render(request, 'index.html', {'dojos': dojos})
def add_dojo(request):
    if len(request.POST['name']) < 1 or len(request.POST['city']) < 1 or len(request.POST['state']) < 1:
        return redirect('/')
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')
def add_ninja(request):
    if len(request.POST['first_name']) < 1 or len(request.POST['last_name']) < 1 or (len(request.POST['dojo']) < 1 or request.POST['dojo'] == 'none'):
        return redirect('/')
    dojo = Dojo.objects.get(id=int(request.POST['dojo']))
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=dojo)
    return redirect('/')