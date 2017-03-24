from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    user_name=models.CharField(max_length=65)
    user_email=models.EmailField(unique=True)
    user_password=models.CharField(max_length=65)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

