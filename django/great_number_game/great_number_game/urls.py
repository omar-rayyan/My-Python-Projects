from django.urls import path
from game import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play_again', views.play_again, name='play_again'),
    path('guess', views.guess, name='guess'),
    path('clear', views.clear, name='clear'),
]