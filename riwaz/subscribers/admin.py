from django.contrib import admin
from .models import Subscribers

# Customised Admin view for Block users List
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('id', 'results','status')
    list_display_links = ('id','results')

    search_fields = ('results',)

admin.site.register(Subscribers, SubscribersAdmin)
