from django.db import models
from django.utils import timezone


class Realtor(models.Model):
    name        = models.CharField(max_length=100)
    photo       = models.ImageField(upload_to='realtors/%Y/%m/%d')
    description = models.TextField(max_length=200, blank=True)
    email       = models.TextField(max_length=200, unique=True)
    phone       = models.IntegerField(unique=True)
    is_mvp      = models.BooleanField(default=False)
    hire_date   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'realtor'
        verbose_name_plural = 'realtors'          
