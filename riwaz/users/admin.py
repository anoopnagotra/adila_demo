# -*- coding: utf-8 -*-
import django.contrib.auth.models
from django.contrib import admin
from django.contrib import auth
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib import messages
from django.db import models


admin.site.unregister(auth.models.Group)


class UserCustomAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    # list_display_links = ('id','email')
    list_display = ['id','name','mobile_number', 'is_premium','seller_margin_addition', 'seller_margin_multiply', 'seller_rating' ,'is_active' ,'premium_seller_tag', 'seller_cod', 'max_allowed_highlight']
    list_filter = ('role', 'is_premium', "seller_rating")

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('name','mobile_number', 'state', 'city', 'country','postal_code',)}),
        ('Role and access', {'fields': ('role', 'is_premium','premium_seller_tag', 'seller_cod', 'seller_margin_addition', 'seller_margin_multiply', 'seller_rating', "max_allowed_highlight")}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active')}
        ),
    )
    search_fields = ('email', 'name', 'mobile_number', 'city', 'state', 'address', 'postal_code')
    ordering = ('email',)
    actions = ['mark_delete_numbers', 'permanent_delete_numbers']

    # def mark_delete_numbers(self, request, queryset):
    #     numbers = Numbers.objects.filter(
    #         user__id__in=queryset.values_list("id", flat=True)
    #     ).exclude(number_status__in=('4', '3'))

    #     if numbers.exists():
    #         numbers.update(number_status='3')
    #         messages.info(request, "Numbers Deleted Successfully")
    #     else:
    #         messages.error(request, "There is no unsold numbers to mark delete")
    # mark_delete_numbers.short_description = "Mark selected Users Numbers as Deleted"

    # def permanent_delete_numbers(self, request, queryset):
    #     numbers = Numbers.objects.filter(
    #         user__id__in=queryset.values_list("id", flat=True)
    #     ).exclude(number_status__in=('4', '3'))

    #     if numbers.exists():
    #         numbers.delete()
    #         messages.info(request, "Numbers Deleted Successfully")
    #     else:
    #         messages.error(request, "There is no unsold numbers to delete")
    # permanent_delete_numbers.short_description = "Delete Users Numbers"




# class Seller(User):

#     class Meta:
#         proxy = True


# class SellerAdmin(UserCustomAdmin):
#     list_filter = ('is_premium', "seller_rating")
#     # list_display = UserCustomAdmin.list_display + ['active_numbers', ]
#     list_display = ['id','name','mobile_number', 'is_premium','seller_margin_addition', 'seller_margin_multiply', 'seller_rating', 'active_numbers', 'is_active', 'premium_seller_tag', 'seller_cod', 'max_allowed_highlight']

#     def get_queryset(self, request):
#         qs = super(SellerAdmin, self).get_queryset(request)
#         qs = qs.annotate(num_count=models.Count('numbers', filter=models.Q(numbers__number_status='1')))
#         qs.admin_order_field = 'active_numbers'
#         return qs.filter(role="seller")

#     def active_numbers(self, obj):
#         return obj.num_count
#     active_numbers.admin_order_field = 'num_count'


admin.site.register(User, UserCustomAdmin)
# admin.site.register(Seller, SellerAdmin)
