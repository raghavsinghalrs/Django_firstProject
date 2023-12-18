from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class reciepe(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True , blank = True)
    reciepe_name = models.CharField(max_length=100)
    reciepe_desc = models.TextField()
    reciepe_addby = models.CharField(max_length=100,default='NA')
    reciepe_images = models.ImageField(upload_to="reciepe")

    
