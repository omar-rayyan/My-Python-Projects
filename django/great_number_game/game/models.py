from django.db import models

class UserManager(models.Manager):
    def create_user(self, username, score):
        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            existing_user.score = score
            existing_user.save()
        else:
            return User.objects.create(username=username, score=score)

class User(models.Model):
    username = models.CharField(max_length=255)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()