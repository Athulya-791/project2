from django.db import models

# Create your models here.

class cdb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=50, null=True, blank=True)
class redb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    password = models.IntegerField(null=True, blank=True)
class cadb(models.Model):
    ctn=models.CharField(max_length=50,null=True,blank=True)
    ctp=models.IntegerField(null=True,blank=True)
    ctq=models.IntegerField(null=True,blank=True)
    ctt=models.IntegerField(null=True,blank=True)

