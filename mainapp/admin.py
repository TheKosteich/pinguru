from django.contrib import admin
from .models import Domains, Locations, Addresses, SystemType, Service, Networks


# Register your models here.

class AddressesAdmin(admin.ModelAdmin):
    list_display = ('address', 'hostname', 'location')
    filter_horizontal = ('service',)
    search_fields = ('address', 'hostname')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


class NetworksAdmin(admin.ModelAdmin):
    filter_horizontal = ('service', 'location',)
    search_fields = ('subnet',)


admin.site.register(Addresses, AddressesAdmin)
admin.site.register(Networks, NetworksAdmin)
admin.site.register(Domains)
admin.site.register(Locations)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SystemType)
