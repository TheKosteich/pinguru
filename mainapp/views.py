from django.shortcuts import render, redirect
from .models import Addresses


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        content = {'addresses': Addresses.objects.all()}
        return render(request, 'mainapp/base.html', content)
    else:
        return redirect('auth/login/')
