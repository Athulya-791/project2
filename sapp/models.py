from django.db import models

# Create your models here.
class sdb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    dis=models.CharField(max_length=50,null=True,blank=True)
    img=models.ImageField(upload_to="profile",null=True,blank=True)
class prodb(models.Model):
    cname=models.CharField(max_length=50,null=True,blank=True)
    sname=models.CharField(max_length=50,null=True,blank=True)
    sdis=models.CharField(max_length=50,null=True,blank=True)
    spr=models.IntegerField(null=True,blank=True)
    sim=models.ImageField(upload_to="profile",null=True,blank=True)
