"""pinguru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

# Imports only for development server
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.index, name='main'),
    path('domain/<int:pk>/', mainapp.DomainUpdate.as_view(), name='domain'),
    path('domain/delete/<int:pk>/', mainapp.DomainDelete.as_view(), name='domain_delete'),
    path('domain/add/', mainapp.DomainCreate.as_view(), name='domain_add'),
    path('domains/', mainapp.DomainsList.as_view(), name='domains_list'),
    path('locations/', mainapp.LocationsList.as_view(), name='locations'),
    # path('services/', mainapp.ServicesList.as_view(), name='services'),
    # path('system-types/', mainapp.SystemTypesList.as_view(), name='system-types'),
    path('address/', include('mainapp.urls', namespace='mainapp')),
    path('subnet/<int:pk>/', mainapp.SubnetUpdate.as_view(), name='subnet'),
    path('subnet/<int:pk>/populate', mainapp.subnet_populate, name='subnet_populate'),
    path('auth/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
