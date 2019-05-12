from django.db import models
from django.urls import reverse


# Domain table
class Domains(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Domains'
        verbose_name = 'Domain'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('domain', kwargs={'pk': self.pk})


# Location table
class Locations(models.Model):
    codename = models.CharField(verbose_name='Location code name', max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Locations'
        verbose_name = 'Location'
        ordering = ['codename']

    def __str__(self):
        return self.codename


# Services list
class Service(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Services'
        verbose_name = 'Service'
        ordering = ['name']

    def __str__(self):
        return self.name


# Networks table
class Networks(models.Model):
    network = models.GenericIPAddressField()
    netmask = models.GenericIPAddressField()
    gateway = models.GenericIPAddressField(blank=True, null=True)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Networks'
        verbose_name = 'Network'
        ordering = ['network']

    def __str__(self):
        netmask = sum(bin(int(block)).count('1') for block in self.netmask.split('.'))
        return f'{self.network}/{netmask}'


# Subnet table
class Subnets(models.Model):
    network = models.ForeignKey(Networks, on_delete=models.CASCADE)
    subnet = models.GenericIPAddressField()
    netmask = models.GenericIPAddressField()
    gateway = models.GenericIPAddressField()
    vlan = models.PositiveSmallIntegerField(null=True, blank=True)
    service = models.ManyToManyField(Service, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Subnets'
        verbose_name = 'Subnet'
        ordering = ['network']

    def __str__(self):
        netmask = sum(bin(int(block)).count('1') for block in self.netmask.split('.'))
        return f'{self.subnet}/{netmask}'

    def get_absolute_url(self):
        return reverse('subnet', kwargs={'pk': self.pk})


# System type list
class SystemType(models.Model):
    type = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Service types'
        verbose_name = 'Service type'
        ordering = ['type']

    def __str__(self):
        return self.type


# IP Address table - main table
class Addresses(models.Model):
    address = models.GenericIPAddressField(unique=True, blank=False)
    hostname = models.CharField(max_length=50, blank=True)
    domain = models.ForeignKey(Domains, on_delete=models.PROTECT, null=True, blank=True)
    network = models.ForeignKey(Subnets, on_delete=models.CASCADE, null=True)
    mac = models.CharField(max_length=17, blank=True)
    location = models.ForeignKey(Locations, on_delete=models.PROTECT, null=True, blank=True)
    service = models.ManyToManyField(Service, blank=True)
    system_type = models.ForeignKey(SystemType, on_delete=models.PROTECT, null=True, blank=True)
    responsible = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Addresses'
        verbose_name = 'Address'
        ordering = ['address']

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('mainapp:address', kwargs={'pk': self.pk})
