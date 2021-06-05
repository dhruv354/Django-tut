from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    roll_no = models.IntegerField()
    course = models.CharField(max_length=40)
