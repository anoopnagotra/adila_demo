from django.db import models
from django.conf import settings

from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from riwaz.city.models import City

# Create your models here.

class RiwazCategory(models.Model):
    name = models.CharField('Goal Name', max_length=500, null=True, blank=True)
    descriptions = models.CharField('Goal descriptions', max_length=5000, null=True, blank=True)

    status =  models.BooleanField(default=False)

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='rel_city')

    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at =models.DateTimeField(blank=True, null=True, default=timezone.now)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rel_payment_paytm')

    class Meta:
        db_table = "category"
        app_label = 'category'
        verbose_name_plural = "Goals"
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

