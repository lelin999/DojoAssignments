from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
	def login(self, postData):
		pattern = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if pattern.match(postData):
			return True
		pass

class Email(models.Model):
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()