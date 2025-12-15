from django.db import models

# Create your models here.
class gebruikers(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    role = models.CharField(max_length=25)
    isSuperuser = models.CharField(max_length=20)