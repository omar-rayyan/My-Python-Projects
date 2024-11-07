from django.db import models
from users.models import User

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["title"] = "Please provide a title for your book."
            return errors
        if len(postData['title']) < 2:
            errors["title"] = "Your book's title should be at least 2 characters."
            return errors
        if len(postData['description']) < 5:
            errors["description"] = "Your book's description should be at least 5 characters."
            return errors
        return errors
    def create_book(self, postData, user):
        return Book.objects.create(title=postData['title'], description=postData['description'], uploaded_by=user)

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name = "books_uploaded", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name = "liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()