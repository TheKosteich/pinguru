from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from django.urls import reverse_lazy

from mainapp.models import Domains, Addresses, Locations, Subnets, Networks
from mainapp.forms import AddressUpdateForm, SubnetUpdateForm, DomainUpdateForm
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from netaddr import IPNetwork, IPAddress


# Create your views here.
def index(request):
    locations = Locations.objects.all()
    subnets = Subnets.objects.all()
    context = {'locations': locations, 'subnets': subnets}
    return render(request, 'mainapp/index.html', context)


# Out IP Addresses list
class AddressesList(ListView):
    model = Addresses
    template_name = 'mainapp/addresses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


# --- Work with domains --->


# Out domains list
class DomainsList(ListView):
    model = Domains
    template_name = 'mainapp/domains.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


# Create domain item
class DomainCreate(CreateView):
    model = Domains
    # fields = '__all__'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


class LocationUpdate(UpdateView):
    pass


class LocationDelete(DeleteView):
    pass


class LocationAdd(CreateView):
    pass

# <--- End Work with locations ---

# --- Work with subnets --->


class SubnetUpdate(UpdateView):
    model = Subnets
    template_name = 'mainapp/subnet.html'
    form_class = SubnetUpdateForm


class SubnetDelete(DeleteView):
    pass


class SubnetAdd(CreateView):
    pass

# <--- End Work with Subnets ---



def address(request):
    return HttpResponseRedirect(reverse('main'))


class AddressUpdate(UpdateView):
    model = Addresses
    template_name = 'mainapp/address.html'
    form_class = AddressUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


# Filtering by location
def location(request, location):
    if request.user.is_authenticated:
        locations = Locations.objects.all()
        addresses = Addresses.objects.filter(location__codename=location)

        # Validating the string parameter "<str:location>" from URL
        if addresses:
            context = {'locations': locations, 'addresses': addresses}
            return render(request, 'mainapp/addresses.html', context)
        else:
            return redirect('mainapp:index')
    else:
        return redirect('auth:login')


# Populating subnet by IP's
def subnet_populate(request, pk):
    db_subnet = get_object_or_404(Subnets, pk=pk)
    subnet = IPNetwork(str(db_subnet))
    for ip in subnet:
        addr = Addresses(address=ip, subnet=db_subnet)
        addr.save()
    return render(request, 'mainapp/populated.html')
