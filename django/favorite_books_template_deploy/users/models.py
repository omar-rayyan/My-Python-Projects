from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters, no special characters allowed."
            return errors
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters, no special characters allowed."
            return errors
        if len(postData['email']) < 1:
            errors["email"] = "Please provide an email address."
            return errors
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "The email address you've entered is invalid."
            return errors
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
            return errors
        if postData['password'] != postData['password-confirmation']:
            errors["password-confirmation"] = "Passwords do not match."
            return errors
        existing_email = User.objects.filter(email=postData['email']).exclude(id=postData.get('id'))
        if existing_email.exists():
            errors["email"] = "This email address was already used before. Please login or use a different email address."
            return errors
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors["email"] = "Please provide an email address."
            return errors
        if len(postData['password']) < 1:
            errors["password"] = "Please provide a password."
            return errors
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "The email address you've entered is invalid."
            return errors
        else:
            user = User.objects.filter(email=postData['email']).first()
            if not user:
                errors["email"] = "No user account with this email address was found. Please register."
                return errors
            else:
                if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                    errors["password"] = "Incorrect password."
                    return errors
        return errors
    def create_user(self, postData):
        hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        return User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashed_password)

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()