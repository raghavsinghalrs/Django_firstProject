from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

class car(models.Model):
    name = models.CharField(max_length=30)
    speed = models.IntegerField()