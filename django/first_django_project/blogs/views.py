from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request, number):
    return HttpResponse(f"placeholder to display the blog number: {number}")
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")
def destroy(request, number):
    return redirect("/blogs")
def json_response(request):
    data = {
        "title": "Sample Blog",
        "content": "This is a sampel content for the blog in JSON format."
    }
    return JsonResponse(data)