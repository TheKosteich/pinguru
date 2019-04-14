from django.contrib import admin
from .models import Domains, Locations, Addresses


# Register your models here.

class AddressesAdmin(admin.ModelAdmin):
    list_display = ('address', 'hostname', 'location')
    # list_display_links = ('address', 'hostname')
    search_fields = ('address', 'hostname')


admin.site.register(Addresses, AddressesAdmin)
admin.site.register(Domains)
admin.site.register(Locations)
