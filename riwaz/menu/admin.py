from django.contrib import admin
from .models import RiwazMenu

# Customised Admin view for Block users List
class RiwazMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','description')
    list_display_links = ('id','name')

    search_fields = ('name',)
    def get_category(self, obj):
        return obj.category.name

admin.site.register(RiwazMenu, RiwazMenuAdmin)
