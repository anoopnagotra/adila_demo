from django.contrib import admin
from .models import RiwazCategory

# Customised Admin view for Block users List
class RiwazCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_display_links = ('id','name')

    search_fields = ('name',)

admin.site.register(RiwazCategory, RiwazCategoryAdmin)
