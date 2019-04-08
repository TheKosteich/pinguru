from django.urls import re_path
import authapp.views as authapp

# Required for Django 2.0 an above
app_name = 'authapp'

urlpatterns = [
    re_path('login/', authapp.login, name='login'),
    re_path('logout/', authapp.logout, name='logout'),
    re_path('register/', authapp.register, name='register'),
    re_path('edit/', authapp.edit, name='edit'),
]
