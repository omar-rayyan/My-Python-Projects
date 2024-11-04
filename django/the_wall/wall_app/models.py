from django.db import models
from users_app.models import User


class MessageManager(models.Manager):
    def message_validator(self, postData):
        errors = {}
        if len(postData['text']) < 5:
            errors["text"] = "Your message should at least be 5 characters."
            return errors
        return errors
    def create_message(self, postData, wall_user, commentor):
        return Message.objects.create(content=postData['text'], user=wall_user, commentor=commentor)

class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if len(postData['text']) < 5:
            errors["text"] = "Your comment should at least be 5 characters."
            return errors
        return errors
    def create_comment(self, postData, message, commentor):
        return Comment.objects.create(content=postData['text'], message=message, commentor=commentor)

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    commentor = models.ForeignKey(User, related_name="commented_messages", on_delete=models.CASCADE, null=True)
    objects = MessageManager()

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    commentor = models.ForeignKey(User, related_name="commented_comments", on_delete=models.CASCADE)
    objects = CommentManager()