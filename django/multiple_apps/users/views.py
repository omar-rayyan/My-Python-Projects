from django.shortcuts import redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("placeholder to display a list of users later.")
def register(request):
    return HttpResponse("placeholder for users to create a new user record.")
def login(request):
    return HttpResponse(f"placeholder for users to log in.")