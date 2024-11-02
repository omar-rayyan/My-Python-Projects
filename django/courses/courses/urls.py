from django.urls import path
from courses_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_course', views.add_course, name='add_course'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('comments/<int:id>', views.view_comments, name='view_comments'),
    path('<int:id>/delete', views.delete_course, name='delete_course'),
    path('delete_course_confirm', views.delete_course_confirm, name='delete_course_confirm'),
    path('comments/<int:id>/delete', views.delete_comment, name='delete_comment'),
]