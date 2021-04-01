from django.contrib import admin
from .models import City

# Customised Admin view for Block users List
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')

    search_fields = ('name',)

admin.site.register(City, CityAdmin)
