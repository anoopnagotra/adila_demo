from django.db import models
from django.conf import settings

from django.utils import timezone
from riwaz.category.models import RiwazCategory
from django.utils.translation import gettext_lazy as _
# Create your models here.

DISH_FEATURE = (
        ('Best Seller', 'Best Seller'),
        ('Signature', 'Signature'),
        ('Regular', 'Regular')
    )

DISH_TYPE = (
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg')
    )

DISH_SERVED = (
        ('Hot', 'Hot'),
        ('Very Hot', 'Hot'),
        ('Cold', 'Cold')
    )
    
class RiwazMenu(models.Model):
    name = models.CharField('Name', max_length=500, null=True, blank=True)
    description = models.CharField('Description', max_length=1000, null=True, blank=True)

    goal = models.ForeignKey(RiwazCategory, on_delete=models.CASCADE, related_name='rel_menu')
    # field_name = models.FileField(upload_to=None, max_length=254, **options)
    status =  models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at =models.DateTimeField(blank=True, null=True, default=timezone.now)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rel_payment_paytm')

    class Meta:
        db_table = "menu"
        app_label = 'menu'
        verbose_name_plural = "Department"
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

