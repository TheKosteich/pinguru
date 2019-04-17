from django.db import models
from django.urls import reverse


# Domain table
class Domains(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Location table
class Locations(models.Model):
    codename = models.CharField(verbose_name='Location code name', max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.codename


# Networks table
class Networks(models.Model):
    subnet = models.GenericIPAddressField()
    netmask = models.GenericIPAddressField()
    gateway = models.GenericIPAddressField()
    vlan = models.PositiveSmallIntegerField()
    service = models.CharField(max_length=100)
    location = models.ManyToManyField(Locations)


# IP Address table - main table
class Addresses(models.Model):
    address = models.GenericIPAddressField(unique=True, blank=False)
    hostname = models.CharField(max_length=50, blank=True)
    domain = models.ForeignKey(Domains, on_delete=models.PROTECT, null=True, blank=True)
    netmask = models.GenericIPAddressField(null=True, blank=True)
    subnet = models.GenericIPAddressField(null=True, blank=True)
    gate = models.GenericIPAddressField(null=True, blank=True)
    vlan = models.PositiveSmallIntegerField(null=True, blank=True)
    mac = models.CharField(max_length=17, blank=True)
    location = models.ForeignKey(Locations, on_delete=models.PROTECT, null=True, blank=True)
    service = models.CharField(max_length=200, blank=True)
    sys_type = models.CharField(max_length=100, blank=True)
    responsible = models.CharField(max_length=100, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Addresses'
        verbose_name = 'Address'
        ordering = ['address']

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('mainapp:address', kwargs={'pk': self.pk})
