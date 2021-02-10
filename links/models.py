from django.db import models
from users.models import User

# Create your models here.
class Link(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	golink = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	visitors = models.IntegerField()
	def __str__(self):
		return self.golink