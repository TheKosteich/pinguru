from django.forms import ModelForm
from mainapp.models import Addresses, Subnets, Domains


class AddressUpdateForm(ModelForm):
    class Meta:
        model = Addresses
        fields = '__all__'
        exclude = ['address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-6'
            field.help_text = ''


# Form for subnet view and update
class SubnetUpdateForm(ModelForm):
    class Meta:
        model = Subnets
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-6'
            field.help_text = ''


# Form for domain view and update
class DomainUpdateForm(ModelForm):
    class Meta:
        model = Domains
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-md-12'
            field.help_text = ''
