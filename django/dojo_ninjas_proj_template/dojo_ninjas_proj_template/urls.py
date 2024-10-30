from django.urls import path
from dojo_ninjas_app import views

urlpatterns = [
    path('', views.index),
    path('add_dojo', views.add_dojo, name='add_dojo'),
    path('add_ninja', views.add_ninja, name='add_ninja'),
]