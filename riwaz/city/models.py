from django.db import models
from django.conf import settings

from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class City(models.Model):
    name = models.CharField('Name', max_length=500, null=True, blank=True)

    status =  models.BooleanField(default=False)

    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at =models.DateTimeField(blank=True, null=True, default=timezone.now)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rel_payment_paytm')

    class Meta:
        db_table = "city"
        app_label = 'city'
        verbose_name_plural = "City"
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

