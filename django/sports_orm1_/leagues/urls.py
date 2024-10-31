from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('initialize', views.make_data, name="make_data"),
]
