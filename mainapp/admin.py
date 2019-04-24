from django.contrib import admin
from .models import Domains, Locations, Addresses, SystemType, Service, Subnets, Networks


# Register your models here.

class AddressesAdmin(admin.ModelAdmin):
    list_display = ('address', 'hostname', 'location')
    filter_horizontal = ('service',)
    search_fields = ('address', 'hostname')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


class SubnetsAdmin(admin.ModelAdmin):
    filter_horizontal = ('service',)
    search_fields = ('subnet',)


admin.site.register(Addresses, AddressesAdmin)
admin.site.register(Subnets, SubnetsAdmin)
admin.site.register(Domains)
admin.site.register(Locations)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SystemType)
admin.site.register(Networks)
