# from django.db import models
# from djgeojson.fields import PointField
from django.contrib.gis.db import models

# Create your models here.

class Location(models.Model):
    id = models.BigIntegerField(primary_key=True)
    place_id = models.CharField(max_length=255, null=True)
    datetaken = models.CharField(max_length=255, null=True)
    dateupload = models.CharField(max_length=255, null=True)
    owner = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    latitude_rnd = models.DecimalField(max_digits=15, decimal_places=10)
    longitude_rnd = models.DecimalField(max_digits=15, decimal_places=10)
    geom = models.PointField(null=True)
