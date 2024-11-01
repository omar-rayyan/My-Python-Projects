from django.shortcuts import render, redirect
from .models import TvShow

def index(request):
    return redirect("/shows")
def display_all_shows(request):
    context = {
        "shows": TvShow.objects.all(),
    }
    return render(request, "all_shows.html", context)
def new_show(request):
    return render(request, "new_show.html")
def add_show(request):
    show = TvShow.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect(f'/shows/{show.id}')
def view_show(request, id):
    show = TvShow.objects.get(id=id)
    request.session['show'] = show.id
    context = {
        "show": show,
    }
    return render(request, 'view_show.html', context)
def delete_show(request, id):
    show = TvShow.objects.get(id=id)
    show.delete()
    return redirect("/shows")
def edit_show(request, id):
    show = TvShow.objects.get(id=id)
    if request.method == 'GET':
        request.session['show'] = show.id
        context = {
            "show": show,
        }
        return render(request, 'edit_show.html', context)
    else:
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return render(request, 'view_show.html', context)