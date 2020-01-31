from django.db import models
from django.utils import timezone

from realtors.models import Realtor


class Listing(models.Model):
    realtor     = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title       = models.CharField(max_length=100)
    address     = models.CharField(max_length=100)
    city        = models.CharField(max_length=100)
    county      = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    price       = models.IntegerField()
    bedrooms    = models.IntegerField()
    bathrooms   = models.DecimalField(max_digits=2, decimal_places=1)
    garage      = models.IntegerField(default=0)
    sqft        = models.IntegerField()
    loot_size   = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main  = models.ImageField(upload_to='houses/%Y/%m/%d')
    photo_1     = models.ImageField(upload_to='houses/%Y/%m/%d', blank=True, null=True)
    photo_2     = models.ImageField(upload_to='houses/%Y/%m/%d', blank=True, null=True)
    photo_3     = models.ImageField(upload_to='houses/%Y/%m/%d', blank=True, null=True)
    photo_4     = models.ImageField(upload_to='houses/%Y/%m/%d', blank=True, null=True)
    photo_5     = models.ImageField(upload_to='houses/%Y/%m/%d', blank=True, null=True)
    photo_6     = models.ImageField(upload_to='houses/%Y/%m/%d', blank=True, null=True)
    is_punlished= models.BooleanField(default=True)
    list_date   = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name        = 'listing'
        verbose_name_plural = 'listings'

    def __str__(self):
        # mainfiled
        return self.title   
