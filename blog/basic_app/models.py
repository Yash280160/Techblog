from django.db import models
from django.utils import timezone

# Create your models here.

class Ask(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length = 15)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)

	def publish(self):
		self.save()

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey('basic_app.Ask', on_delete = models.CASCADE,related_name = 'comments')
	author = models.CharField(max_length = 20)
	created_date = models.DateTimeField(default = timezone.now)
	text = models.TextField()
	approved_comment = models.BooleanField(default = False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def approved_comments(self):
		return self.comments.filter(approved_comment = True)

	def __str__(self):
		return self.text










