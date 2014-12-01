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
	