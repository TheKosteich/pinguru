from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'avatar', 'department')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    # def clean_department(self):
    #     in_department = self.cleaned_data['department']
    #     if in_department not in ['OZI', 'UMASIT']:
    #         raise forms.ValidationsError('Доступ для вашего департамента запрещен!')
    #
    #     return in_department


class CustomUserEditForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'email', 'department', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    # def clean_department(self):
    #     in_department = self.cleaned_data['department']
    #     if in_department not in ['OZI', 'UMASIT']:
    #         raise forms.ValidationsError('Доступ для вашего департамента запрещен!')
    #
    #     return in_department
