from django.urls import path
from wall_app import views

urlpatterns = [
    path('', views.redirect_to_home_wall, name='redirect_to_home_wall'),
    path('<int:id>', views.view_wall, name='view_wall'),
    path('post_message', views.post_message, name='post_message'),
    path('<int:id>/delete_message', views.delete_message, name='delete_message'),
    path('<int:id>/delete_comment', views.delete_comment, name='delete_comment'),
    path('post_comment', views.post_comment, name='post_comment'),
]