from __future__ import unicode_literals

from django.db import models
from django.utils import timezone as django_tz 

from owner.models import Owner

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=200,unique=True,blank=False)
	ruc  = models.CharField(max_length=11,unique=True)
	owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
	createdAt = models.DateTimeField(
        	'Starting time for the rule', default=django_tz.now, blank=True
	)
