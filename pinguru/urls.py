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

    # --- Domain URLs --->
    path('domain/<int:pk>/', mainapp.DomainUpdate.as_view(), name='domain'),
    path('domain/<int:pk>/delete/', mainapp.DomainDelete.as_view(), name='domain_delete'),
    path('domain/add/', mainapp.DomainCreate.as_view(), name='domain_add'),
    path('domains/', mainapp.DomainsList.as_view(), name='domains_list'),
    # <--- End Domain URLs ---

    # --- Location URLs --->
    path('location/<int:pk>/', mainapp.LocationUpdate.as_view(), name='location'),
    path('location/<int:pk>/delete/', mainapp.LocationDelete.as_view(), name='location_delete'),
    path('location/add/', mainapp.LocationAdd.as_view(), name='location_add'),
    path('locations/', mainapp.LocationsList.as_view(), name='locations'),
    # <--- End Location URLs ---

    # --- Subnet URLs --->
    path('subnet/<int:pk>/', mainapp.SubnetUpdate.as_view(), name='subnet'),
    path('subnet/<int:pk>/delete/', mainapp.SubnetDelete.as_view(), name='subnet'),
    path('subnet/add/', mainapp.SubnetAdd.as_view(), name='subnet'),
    # <--- End Subnet URLS ---

    # path('services/', mainapp.ServicesList.as_view(), name='services'),
    # path('system-types/', mainapp.SystemTypesList.as_view(), name='system-types'),
    path('address/', include('mainapp.urls', namespace='mainapp')),
    path('auth/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
