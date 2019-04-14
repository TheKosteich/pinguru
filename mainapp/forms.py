from django.forms import ModelForm
from mainapp.models import Addresses


class AddressUpdate(ModelForm):
    class Meta:
        model = Addresses
        fields = '__all__'
