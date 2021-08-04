from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime , date

class BgModel(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	body = RichTextField(blank = True, null = True)
	#body = models.TextField()
	post_updated = models.DateTimeField(auto_now = True)
	post_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	class Meta:
		ordering = ('-post_updated',)

