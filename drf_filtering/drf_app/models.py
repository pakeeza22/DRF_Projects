from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=200)
    passby = models.CharField(max_length=200)
