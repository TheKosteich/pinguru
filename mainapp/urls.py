from django.urls import path
from mainapp.views import address, AddressUpdate

# Required for Django 2.0 an above
app_name = 'mainapp'

urlpatterns = [
    path('', address, name='index'),
    path('<int:pk>/', AddressUpdate.as_view(), name='address'),
]