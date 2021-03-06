from django.urls import path
from mainapp.views import AddressesList, AddressUpdate #, location

# Required for Django 2.0 an above
app_name = 'mainapp'

urlpatterns = [
    path('', AddressesList.as_view(), name='index'),
    path('<int:pk>/', AddressUpdate.as_view(), name='address'),
    # path('<str:location>/', location, name='location'),
    path('<str:location>/', AddressesList.as_view(), name='location'),
]
