from django.db import models

# Create your models here.
class Location(models.Model):
    locationName = models.CharField(max_length=30)
