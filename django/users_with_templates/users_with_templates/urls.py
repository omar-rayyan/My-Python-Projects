from django.urls import path
from users_app import views

urlpatterns = [
    path('', views.index),
    path('add_user', views.add_user, name='add_user'),
]