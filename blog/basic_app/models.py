from django.db import models
from django.utils import timezone

# Create your models here.

class Ask(models.Model):
	author = models.CharField(max_length = 20)
	title = models.CharField(max_length = 15)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)

	def publish(self):
		self.save()

	def __str__(self):
		return self.title



