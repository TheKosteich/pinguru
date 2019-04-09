from django.contrib import admin
from .models import Domains, Locations, Addresses

# Register your models here.
admin.site.register(Addresses)
admin.site.register(Domains)
admin.site.register(Locations )
