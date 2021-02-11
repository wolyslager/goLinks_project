from django.db import models

# Create your models here.
class Link(models.Model):
	user = models.CharField(max_length=200)
	golink = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	visitors = models.IntegerField()
	def __str__(self):
		return self.golink