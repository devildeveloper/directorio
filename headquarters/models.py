from __future__ import unicode_literals

from django.db import models
from django.utils import timezone as django_tz

from company.models  import Company

# Create your models here.
class HeadQuarters(models.Model):
	services  = models.CharField(max_length=200,blank=False)
	address = models.CharField(max_length=200,blank=False)
	lat = models.DecimalField(max_digits=9,decimal_places=6,help_text="latitude of headquarter")
	lng = models.DecimalField(max_digits=9,decimal_places=6,help_text="longitude of headquarter")
	parking = models.BooleanField(default=False,help_text="has parking?")
	website = models.CharField(max_length=200,blank=True,help_text='headquarter website')
	reservation = models.BooleanField(default=False,help_text='allow reservation?')
	phone = models.CharField(max_length=200,help_text='cellphone, in house phone')	
	company = models.ForeignKey(Company,on_delete=models.CASCADE)
        createdAt = models.DateTimeField(
                'Starting time for the rule', default=django_tz.now, blank=True
        )	
