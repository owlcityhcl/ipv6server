"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from eth_photo import views as eth_photo_views 
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.home,name='login'),
    url(r'^index/$',views.get_pass,name='login'),
    url(r'^upload/$',views.UploadedImageView,name='upload'),
    url(r'^success/$',views.success,name='success'),
    url(r'^webSearch/$',views.webSearch,name='search'),
    url(r'^Latin_operatio_record/$',views.Search_recoder),
    url(r'^login/$',eth_photo_views.app_login,name='app_login'),
]
