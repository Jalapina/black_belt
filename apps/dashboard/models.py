from __future__ import unicode_literals

from django.db import models
from ..main.models import User
class Quote(models.Model):
    quote_by=models.CharField(max_length=50)
    quote=models.TextField(max_length=1000)
    quote_creator=models.ForeignKey(User)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Favorite(models.Model):
    favorite=models.ForeignKey(Quote, related_name='fav')
    user_fav=models.ForeignKey(User)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

