from django.db import models
from django.contrib.auth.models import User

# create models here
class Topic(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Discussion(nodels.Model):
    discussion_text = models.TextField(max_length=3000)
    created_on_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(null=True)
    topic = models.ForeignKey(Topic, related_name='discussions', on_delete=models.CASCADE)
    discussion_author = models.ForeignKey(User, related_name='discussions', on_delete=models.CASCADE)


class Reply(models.Model):
    message - models.CharField(max_length=255)
    discussion = models.ForeignKey(Discussion, related_name='replies', on_delete=models.CASCADE)
    created_on_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(null=True)
    created_by = models.ForgeinKey(User, related_name='replies', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)