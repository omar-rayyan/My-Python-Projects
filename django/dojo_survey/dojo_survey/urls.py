# project urls.py
from django.urls import path
from survey import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.display_result, name='display_result'),
    path('go_back', views.go_back, name='go_back'),
]