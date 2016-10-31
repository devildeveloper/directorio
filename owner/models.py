from __future__ import unicode_literals

from django.db import models
from django.utils import timezone as django_tz

# Create your models here.
class Owner(models.Model):
        name = models.CharField(max_length=200,unique=True,blank=False)
        email = models.EmailField(max_length=100,unique=True)
	phone = models.CharField(max_length=20,unique=True,blank=False)
        createdAt = models.DateTimeField(
                'Starting time for the rule', default=django_tz.now, blank=True
        )
