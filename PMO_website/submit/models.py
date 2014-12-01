from django.db import models

# Create your models here.
from django.db import models
import datetime
import os
from django.utils import timezone
from datetime import datetime


def file(self, filename):
	url = "documents/groups/%s/%s" %(self.group_name, filename)
	
	return url

def hashed_uploads_dirs(instance, filename):
    """Returns path with md5 hash as directory"""
    return os.path.join(instance.md5, filename)




class Groups(models.Model):
	group_name = models.CharField(max_length=200)
	sub_date = models.DateTimeField('date published',null=True, blank=True)
	
	published = models.CharField(max_length=255, null=True, blank=True)
	
	docfile = models.FileField(upload_to=file,null=True, blank=True)		
	
	md5 = models.CharField(max_length=32,null=True, blank=True)
	summary = models.TextField(max_length=500, null=True, blank=True)
	src_url = models.URLField(null=True, blank=True)
	doc_url = models.URLField(null=True, blank=True)
	
	def file_location(self):
		return self.docfile
				
		
	def __str__(self):              # __unicode__ on Python 2
		return self.group_name
		
	
		
	
class Partners(models.Model):
	group = models.ForeignKey(Groups)
	partner_name = models.CharField(max_length=200,null=True, blank=True)
	
	
	def __str__(self):              # __unicode__ on Python 2
		return self.partner_name


	
		
