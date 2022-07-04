"""uptact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from contacts import views as contacts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contacts_views.list_contacts, name='list_contacts'),
    path('contacts/add/', contacts_views.add_contact, name='add_contact'),
    path('contacts/<int:pk>/edit/',
         contacts_views.edit_contact,
         name='edit_contact'),
    path('contacts/<int:pk>/delete/',
         contacts_views.delete_contact,
         name='delete_contact'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
