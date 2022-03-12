from django.db import models

# Create your models here.
class Unit(models.Model):
    title =  models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=250,blank=False, default='')
      