from django.urls import path, include
from users_app import views

urlpatterns = [
    path('', views.root, name='root'),
    path('users/', include('users_app.urls')),
    path('wall/', include('wall_app.urls')),
]