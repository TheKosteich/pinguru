from django import forms


class AddressForm(forms.Form):
    address = forms.GenericIPAddressField(help_text='Enter IP address')

    # class Meta:
    #     model = CustomUser
    #     fields = ('username', 'password')
    #
    # def __init__(self, *args, **kwargs):
    #     super(CustomUserLoginForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control form-control-user'
    #         if field_name == 'username':
    #             field.widget.attrs['placeholder'] = 'Enter username'
    #         elif field_name == 'password':
    #             field.widget.attrs['placeholder'] = 'Enter password'
    #         else:
    #             pass
