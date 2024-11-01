from django.db import models
from datetime import datetime

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters."
            return errors
        existing_show = TvShow.objects.filter(title=postData['title']).exclude(id=postData.get('id'))
        if existing_show.exists():
            errors["title"] = "A show with this title already exists."
            return errors
        if len(postData['network']) < 3:
            errors["description"] = "Network name should be at least 3 characters."
            return errors
        if not postData.get('release_date'):
            errors["release_date"] = "Release date is required."
            return errors
        if len(postData['description']) > 1 and len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters."
            return errors
        release_date = datetime.strptime(postData['release_date'], "%Y-%m-%d").date()
        if release_date > datetime.today().date():
            errors["release_date"] = "Release date cannot be in the future."
            return errors
        return errors

class TvShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()