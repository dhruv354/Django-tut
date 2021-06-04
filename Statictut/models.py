from django.db import models

# Create your models here.

class details(models.Model):
    name =  models.CharField(max_length=30)
    img = models.ImageField(default='')
    age = models.IntegerField(default=-1)
    pub_date = models.DateField()

