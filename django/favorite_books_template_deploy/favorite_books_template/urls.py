from django.urls import path, include

urlpatterns = [
    path('books/', include('books.urls')),
    path('', include('users.urls')),
]