from django.db import models


# Create your models here.
class users(models.Model):
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
