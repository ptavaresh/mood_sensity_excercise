from django.db import models

from django.contrib.gis.db import models


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):             
      return self.name

class Picture(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
  picture = models.FileField(blank=False, null=False)
  latitude = models.FloatField()
  longitude = models.FloatField()
  timestamp = models.DateTimeField(auto_now_add=True)
  mood = models.CharField(max_length=20)