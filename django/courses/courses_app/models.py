from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be at least 5 characters."
            return errors
        existing_course = Course.objects.filter(name=postData['name']).exclude(id=postData.get('id'))
        if existing_course.exists():
            errors["name"] = "A course with this name already exists."
            return errors
        if len(postData['description']) < 15:
            errors["description"] = "Course description should be at least 15 characters."
            return errors
        return errors

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['text']) < 5:
            errors["text"] = "Your comment should be at least 4 characters."
            return errors
        return errors

class Description(models.Model):
    content = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CommentManager()