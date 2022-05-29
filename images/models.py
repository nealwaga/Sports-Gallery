from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class categories(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Image(models.Model):
    name= models.CharField(max_length=50)
    description = HTMLField()
    gallery_image = models.ImageField(upload_to='articles/', blank=True)
    categories = models.ManyToManyField(categories)
    location = models.ManyToManyField(location)