from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from .models import Addresses
from django.views.generic.edit import UpdateView


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        content = {'addresses': Addresses.objects.all()}
        return render(request, 'mainapp/index.html', content)
    else:
        return redirect('auth/login/')


def address(request, pk=None):
    if pk:
        current_address = get_object_or_404(Addresses, pk=pk)
        context = {
            'address': current_address,
        }
        return render(request, 'mainapp/address.html', context)
    else:
        return HttpResponseRedirect(reverse('main'))


class AddressUpdate(UpdateView):
    model = Addresses
    fields = '__all__'
    template_name = 'mainapp/address.html'
