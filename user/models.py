from django.db import models

# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=12)
    email = models.CharField(max_length=26)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)
