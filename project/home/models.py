from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
		post = models.CharField(max_length=500)
		image = models.FileField(null=True, blank=True)
		user = models.ForeignKey(User, 'on_delete')
		created = models.DateTimeField(auto_now_add=True)
		updated = models.DateTimeField(auto_now=True)


