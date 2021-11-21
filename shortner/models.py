from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=1000000)
    uuid = models.CharField(max_length=10)

class long(models.Model):
    name = models.CharField(max_length=1000)
    eric = models.CharField(max_length=10)