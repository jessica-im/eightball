from django.db import models

# Create your models here.
class Place(models.Model):
    locationName = models.CharField(max_length=100)
    locationAddress = models.CharField(max_length=100)
    locationCity = models.CharField(max_length=100)
    locationState = models.CharField(max_length=100)
    tableSize = models.CharField(max_length=100)
    tableBrand = models.CharField(max_length=100)
    tableCondition = models.CharField(max_length=100)
    cueCondition = models.CharField(max_length=100)
    vibe = models.CharField(max_length=100)
    newFriends = models.CharField(max_length=100)
