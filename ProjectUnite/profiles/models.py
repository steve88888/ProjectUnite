from django.db import models
from django.contrib.auth.models import User

class SignUp(models.Model):
	#user = models.ForeignKey(SignUp)
	email = models.EmailField()
	user = models.ForeignKey(User)
		
	full_name = models.CharField(max_length=40)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
		#might need text widget
	skills = models.TextField()
		#Qualifications = models.TextField()
	Experience = models.TextField()
	CurrentDegree = models.CharField(max_length=40, blank = True, null = True)
	Currentprojects = models.TextField()
	location = models.CharField(max_length=40)
	active = models.BooleanField(default = True)

		
	def __unicode__(self):
		return self.email
# Create your models here.

#class SearchProfiles(models.Model):

class UserPicture(models.Model):
	user = models.ForeignKey(User)
	image = models.ImageField(upload_to='profiles/')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	active = models.BooleanField(default = True)
	thumbnail = models.BooleanField(default = False)
	def __unicode__(self):
		return str(self.image)