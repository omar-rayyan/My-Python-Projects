from django.urls import path, include
from books import views

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('<int:id>', views.view_book, name='view_book'),
    path('add_book', views.add_book, name='add_book'),
    path('edit_book', views.edit_book, name='edit_book'),
    path('go_back', views.all_books, name='go_back'),
    path('favorite_book_view_all_books/<int:book_id>', views.favorite_book_view_all_books, name='favorite_book_view_all_books'),
    path('favorite_book_view_book/<int:book_id>', views.favorite_book_view_book, name='favorite_book_view_book'),
]