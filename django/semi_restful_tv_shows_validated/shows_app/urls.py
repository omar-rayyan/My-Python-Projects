from django.urls import path     
from . import views

urlpatterns = [
    path('', views.display_all_shows, name='display_all_shows'),
    path('new', views.new_show, name='new_show'),
    path('add_show', views.add_show, name='add_show'),
    path('comments/<int:id>', views.view_show, name='view_show'),
    path('<int:id>/edit', views.edit_show, name='edit_show'),
    path('<int:id>/delete', views.delete_show, name='delete_show'),
]
