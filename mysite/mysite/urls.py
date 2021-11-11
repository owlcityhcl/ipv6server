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
from django.urls import path,include

from django.views.static import serve
from . import settings 


urlpatterns = [
    path('home/',eth_photo_views.home,name='home'),
    path(r'',include('eth_photo.urls')),
    path('test_login/',eth_photo_views.test_login,name='test_login'),
    path('login/',eth_photo_views.app_login,name='app_login'),
    url(r'^webLogin/',include('eth_photo.urls')),
    path('admin/', admin.site.urls),
    path('search/',eth_photo_views.search),
    path('img_request/',eth_photo_views.img_request),


    # path('imgView/',eth_photo_views.index),
    # path('api',eth_photo_views.api),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

