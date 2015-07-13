from django.db import models
from django.contrib.auth.models import User

class ProjectTitle(models.Model):
	user = models.ForeignKey(User)
	projectID = models.AutoField(primary_key=True)
	
	title = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	contact_email = models.EmailField()
	description = models.TextField()
	team_members = models.CharField(max_length = 100)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default = True)

	def __unicode__(self):
		return self.title


# Create your models here.

#class searchProject(models.Model):
