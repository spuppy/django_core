from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(null=True,blank=True)

	def __unicode__(self):
		return self.name