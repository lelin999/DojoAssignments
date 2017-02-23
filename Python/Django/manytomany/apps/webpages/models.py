from __future__ import unicode_literals
from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
	def validate(self, postData):
		pattern = re.compile('^[a-zA-Z]{2,}$')
		if pattern.match(postData['name']) and pattern.match(postData['interest']):
			User.objects.create(name=postData['name'])
			return (True, 'hue')
		else:
			return (False, 'Invalid input')
			# use 'add' to link interests to Users
			# run for loop 

class User(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Interest(models.Model):
	interest = models.CharField(max_length=255)
	user_int = models.ManyToManyField(User, related_name='interest')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()