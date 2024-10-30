from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<int:number>', views.show, name='show'),
    path('<int:number>/edit', views.edit, name='edit'),
    path('<int:number>/delete', views.destroy, name='destroy'),
    path('json', views.json_response, name='json_response'),
]