# survey/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('result', views.display_result, name='display_result'),
    path('go_back', views.go_back, name='go_back'),
]