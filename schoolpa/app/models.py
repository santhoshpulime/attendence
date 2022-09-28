from django.db import models
from django.contrib.auth.models import User,auth
from  datetime import datetime


class student(models.Model):
	studentname = models.TextField()
	rollnumber = models.TextField()
	phonenumber = models.TextField()
	studentclass = models.TextField(null=True,blank=True)
class classroom(models.Model):
	c = models.TextField()

class attendance(models.Model):
	studentname = models.TextField()
	pre_abs = models.TextField(blank=True)
	timedata = models.DateTimeField(auto_now_add=True,blank=True)


	
