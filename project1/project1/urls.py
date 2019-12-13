"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from tournaments.views import main
from rest_framework.authtoken import views
from rest_framework_jwt import authentication
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', main, name='main'),
    path('jwt_auth/', obtain_jwt_token),
    path('auth/', views.obtain_auth_token),
    path('tournaments/', include('tournaments.urls', namespace='tournaments')),
    path('battles/', include('battles.urls', namespace='battles'))
]
