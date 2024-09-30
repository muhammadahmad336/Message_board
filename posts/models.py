from django.db import models
# from django.contrib.auth.models import user
from core import settings
# Create your models here.

class  post(models.Model):
       auth = models.ForeignKey(settings.AUTH_USER_MODEL, )
       title= models.CharField(max_length=100)
       body = models.TextField() 

     #   def  __str__(self):
     #        return self.body[:50]