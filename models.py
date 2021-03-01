from django.db import models

# Create your models here.
class about(models.Model):

    summary = models.CharField(max_length = 500)

# class Dest:
#     id : int
#     name: str

class Project(models.Model):
    name = models.CharField(max_length = 100,default = None)
    img = models.ImageField(upload_to= 'pics',default = None)
    description = models.CharField(max_length = 200, default=None )
    link = models.URLField(max_length = 200,default = None)

class Skills(models.Model):
    name = models.CharField(max_length =100, default = None)
    imgs = models.ImageField(upload_to= 'pics',default = None)
    
class Say(models.Model):
    name = models.CharField(max_length = 100,default = None)
    phone = models.BigIntegerField()
    email = models.EmailField()
    message = models.CharField(max_length = 500, default = None)



