from django.db import models


# Domain table
class Domains(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)


# Location table
class Locations(models.Model):
    codename = models.CharField(verbose_name='Location code name', max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)


# IP Address table - main table
class Addresses(models.Model):
    hostname = models.CharField(max_length=50)
    domain = models.ForeignKey(Domains, on_delete=models.CASCADE)
    address = models.GenericIPAddressField()
    netmask = models.GenericIPAddressField()
    subnet = models.GenericIPAddressField()
    mac = models.CharField(max_length=17, unique=True)
    gate = models.GenericIPAddressField()
    vlan = models.PositiveSmallIntegerField()
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    service = models.CharField(max_length=200)
    sys_type = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.address
