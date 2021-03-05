from django.db import models

# Create your models here.
class about(models.Model):

    summary = models.TextField(default = None)

class Project(models.Model):
    name = models.CharField(max_length = 100,default = None)
    img = models.ImageField(upload_to= 'pics',default = None)
    description = models.TextField(default=None )
    link = models.URLField(max_length = 200,default = None)

class Skills(models.Model):
    name = models.CharField(max_length =100, default = None)
    imgs = models.ImageField(upload_to= 'pics',default = None)
    
class Say(models.Model):
    name = models.CharField(max_length = 100,default = None)
    subject = models.CharField(max_length = 200,default = None)
    email = models.EmailField()
    message = models.TextField( default = None)
class Resume(models.Model):
    upload = models.FileField(upload_to='uploads',default = None)




