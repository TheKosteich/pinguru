from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from mainapp.models import Domains, Addresses, Locations, Subnets, Networks
from mainapp.forms import AddressUpdateForm, SubnetUpdateForm, DomainUpdateForm, LocationUpdateForm
from netaddr import IPNetwork, IPAddress


# Create your views here.
def index(request):
    locations = Locations.objects.all()
    subnets = Subnets.objects.all()
    context = {'locations': locations, 'subnets': subnets}
    return render(request, 'mainapp/index.html', context)


# --- Work with addresses --->
# Out IP Addresses list
class AddressesList(ListView):
    model = Addresses
    template_name = 'mainapp/addresses.html'
    # To use paginator in ClassView
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        if self.kwargs and self.kwargs['location']:
                context['object_list'] = Addresses.objects.filter(location__codename=self.kwargs['location'])
        return context


class AddressUpdate(UpdateView):
    model = Addresses
    template_name = 'mainapp/address.html'
    form_class = AddressUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context

# <--- End work with addresses ---


# --- Work with domains --->
# Out domains list
class DomainsList(ListView):
    model = Domains
    template_name = 'mainapp/domains.html'
    # To use paginator in ClassView
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


# Create domain item
class DomainCreate(CreateView):
    model = Domains
    form_class = DomainUpdateForm
    template_name = 'mainapp/domain-add.html'
    success_url = reverse_lazy('domains_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


class DomainUpdate(UpdateView):
    model = Domains
    template_name = 'mainapp/domain.html'
    form_class = DomainUpdateForm
    success_url = reverse_lazy('domains_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


class DomainDelete(DeleteView):
    model = Domains
    success_url = reverse_lazy('domains_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context
# <--- End Work with domains ---


# --- Work with locations --->
# Out locations list
class LocationsList(ListView):
    model = Locations
    template_name = 'mainapp/locations.html'
    # To use paginator in ClassView
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


class LocationUpdate(UpdateView):
    model = Locations
    template_name = 'mainapp/location.html'
    form_class = LocationUpdateForm
    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


class LocationDelete(DeleteView):
    model = Locations
    success_url = 'locations_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


class LocationCreate(CreateView):
    model = Locations
    form_class = LocationUpdateForm
    template_name = 'mainapp/location-add.html'
    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context
# <--- End Work with locations ---


# --- Work with subnets --->
class SubnetUpdate(UpdateView):
    model = Subnets
    template_name = 'mainapp/subnet.html'
    form_class = SubnetUpdateForm
    success_url = reverse_lazy('main')


class SubnetDelete(DeleteView):
    model = Subnets
    success_url = reverse_lazy('main')


class SubnetCreate(CreateView):
    model = Subnets
    form_class = SubnetUpdateForm
    success_url = reverse_lazy('main')
    template_name = 'mainapp/subnet-add.html'


# Populating subnet by IP's
# TODO: Include this feature to SubnetCreate Class View
def subnet_populate(request, pk):
    db_subnet = get_object_or_404(Subnets, pk=pk)
    subnet = IPNetwork(str(db_subnet))
    for ip in subnet:
        if ip != subnet.network and ip != subnet.broadcast:
            try:
                address = Addresses.objects.get(address=str(ip))
                pass
            except Addresses.DoesNotExist:
                address = Addresses(address=str(ip), network=db_subnet)
                address.save()
    return redirect('/')


# <--- End Work with Subnets ---
