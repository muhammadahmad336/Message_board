from django.db import models

# Create your models here.

class  post(models.Model):
       body = models.TextField(max_length=50) 

       def  __str__(self):
            return self.body