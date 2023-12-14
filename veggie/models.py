from django.db import models

# Create your models here.

class reciepe(models.Model):
    reciepe_name = models.CharField(max_length=100)
    reciepe_desc = models.TextField()
    reciepe_images = models.ImageField(upload_to="reciepe")
    
