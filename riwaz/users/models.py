from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager

from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.mail import EmailMessage


USER_TYPE = (
        ('user', 'user'),
        ('seller', 'seller'),
        ('admin', 'admin')
    )

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=100, unique=False, blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    name = models.CharField(max_length=200,blank=False)
    mobile_number = models.CharField(max_length=20,blank=True)
    primary_number = models.CharField(max_length=20,blank=True)
    
    mobile_number_verified =  models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
   
    address = models.TextField(max_length=200,blank=True)
    city = models.CharField(max_length=120,blank=True)
    state = models.CharField(max_length=120,blank=True)
    country = models.CharField(max_length=120,blank=True)
    postal_code = models.CharField(max_length=20,blank=True)
    total_purchases = models.CharField(max_length=20,blank=True)
    forgot_password_token = models.CharField(max_length=100,blank=True)
    mobile_verify_token = models.CharField(max_length=100,blank=True)
    email_verify_token = models.CharField(max_length=100,blank=True)
    
    status = models.BooleanField(default=False)
    premium_seller_tag = models.BooleanField(default=False)
    seller_cod = models.BooleanField(default=False)

    seller_rating = models.CharField(max_length=5, default=0)

    seller_margin_multiply = models.CharField(max_length=10, default=1.32)
    
    seller_margin_addition = models.CharField(max_length=10, default='550')

    is_premium = models.BooleanField(default=False, help_text="Seller is Premium or Basic", verbose_name=" Is Premium")
    role = models.CharField(choices=USER_TYPE, default='user', max_length=250, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at =models.DateTimeField(auto_now=True, editable=False)
    max_allowed_highlight = models.PositiveIntegerField(default=3)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.name

