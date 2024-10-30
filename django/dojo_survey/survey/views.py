from django.shortcuts import redirect, render

def root(request):
    return redirect("/")
def index(request):
    return render(request, 'dojo_survey.html')
def display_result(request):
    if request.method == "POST":
        likes_mansaf = 'Yes' if 'likesMansaf' in request.POST else 'No'
        context = {
            "name": request.POST['name'],
            "location": request.POST['location'],
            "favorite_language": request.POST['favoriteLanguage'],
            "gender": request.POST['gender'],
            "comment": request.POST['comment'],
            "likesMansaf": likes_mansaf,
        }
        request.session['form_data'] = context
        return redirect('display_result')
    context = request.session.get('form_data')
    if context is None:
        return redirect("/") 
    return render(request, "result.html", context)
def go_back(request):
    return redirect("/")