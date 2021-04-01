from django.db import models
from django.utils import timezone
from riwaz.menu.models import RiwazMenu
from django.utils import timezone

class Subscribers(models.Model):
    results = models.CharField(max_length=4600,blank=True)

    department = models.ForeignKey(RiwazMenu, on_delete=models.CASCADE, related_name='rel_department')
    
    status =  models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at =models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return self.results

    class Meta:
        db_table = "subscribers"
        verbose_name_plural = "Results"

class RiwazSubscribers(models.Model):
    customer_name = models.CharField(max_length=200,blank=False)
    customer_email = models.CharField(max_length=200,blank=False)
    # customer_email = models.EmailField(_('email address'), unique=False,blank=True)
    customer_mobile = models.CharField(max_length=20,blank=True)
    subject = models.CharField(max_length=300,blank=True)
    message1 = models.CharField(max_length=1000,blank=True)
    message2 = models.CharField(max_length=1000,blank=True)
    message3 = models.CharField(max_length=1000,blank=True)
    
    data_from = models.CharField(max_length=50,blank=True)

    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at =models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        db_table = "customers"
        app_label = 'customers'
        verbose_name_plural = "Riwaz Reserve Customers"
    
    def __unicode__(self):
        return self.customer_name

    def __str__(self):
        return self.customer_name