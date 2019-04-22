from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from mainapp.models import Addresses, Locations
from mainapp.forms import AddressUpdateForm
from django.views.generic.edit import UpdateView


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        locations = Locations.objects.all()
        addresses = Addresses.objects.all()
        context = {'locations': locations, 'addresses': addresses}
        return render(request, 'mainapp/index.html', context)
    else:
        return redirect('auth/login/')


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
            return render(request, 'mainapp/index.html', context)
        else:
            return redirect('main')
    else:
        return redirect('auth:login')
