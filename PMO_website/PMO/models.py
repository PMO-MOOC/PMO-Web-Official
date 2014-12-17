from django.db import models

# Create your models here.
from django.db import models
import datetime
import os
#from django.utils import timezone
from datetime import datetime


class User(models.Model):
	recent_upload = models.TextField(max_length=500, null=True, blank=True)
	
	pub_date = models.DateTimeField('date published', null=True, blank=True)
	user_name = models.CharField(max_length=200, null=True, blank=True)
	
class Question(models.Model):
	question_id = models.AutoField(max_length=1000,primary_key=True)
        question = models.TextField(null=False,blank=False)
	ques_date = models.DateTimeField()
	userr = models.ForeignKey(User) 

	def __str__(self):             
            return self.question

class Post(models.Model):
        ques_id = models.ForeignKey(Question)    
	userr = models.ForeignKey(User)  
	post = models.TextField(max_length=500, null=True, blank=True)
	post_date = models.DateTimeField()

	def __str__(self):             
            return self.post
