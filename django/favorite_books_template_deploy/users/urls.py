from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.root, name='root'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]