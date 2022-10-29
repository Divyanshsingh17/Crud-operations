from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    # age = models.IntegerField(max_length = 3)
