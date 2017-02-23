from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
	message = models.TextField()
	user_id = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	user_id = models.ForeignKey(User)
	message_id = models.ForeignKey(Message)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)		
