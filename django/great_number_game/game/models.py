from django.db import models

class UserManager(models.Manager):
    def create_user(self, username, score):
        existing_username = User.objects.filter(username=username)
        if existing_username.exists():
            existing_username.score = score
        else:
            return User.objects.create(username=username, score=score)

class User(models.Model):
    username = models.CharField(max_length=255)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()