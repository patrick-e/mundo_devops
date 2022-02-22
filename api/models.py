
from django.db import models

# Create your models here.


class Data(models.Model):
    query = models.CharField(max_length=12)
    status = models.CharField(max_length=7)
    continent =  models.CharField(max_length=20)
    continentcode =  models.CharField(max_length=2)
    country = models.CharField(max_length=30)
    countryCode = models.CharField(max_length=5)
    region = models.CharField(max_length=2)
    regionName = models.CharField(max_length= 40)
    city = models.CharField(max_length=50)
    district =  models.CharField(max_length=90)
    zip = models.CharField(max_length=30)
    lat =  models.FloatField() 
    lon =  models.FloatField()
    timezone =  models.CharField(max_length=20) 
    offset =  models.IntegerField(null=True)
    currency =  models.CharField(max_length=5) 
    isp =  models.CharField(max_length=50) 
    org =  models.CharField(max_length=30) 
    as_query = models.CharField(max_length=50)
    asname =  models.CharField(max_length=40) 
    reverse =  models.CharField(max_length=40) 
    mobile =  models.BooleanField(null=True)
    proxy =  models.BooleanField(null=True)
    hosting =  models.BooleanField(null=True)
    query =  models.CharField(max_length=12) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    




