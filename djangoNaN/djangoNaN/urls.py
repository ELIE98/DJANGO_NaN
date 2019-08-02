"""djangoNaN URL Configuration

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
from django.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from django import views as vs
from django.conf.urls import url
from Game import views

urlpatterns = [

    url('^Game/',include('Game.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^register$',views.register,name='register'),
    url(r'^paris$',views.paris,name='paris'),
    url(r'^login$',auth_views.LoginView.as_view(template_name='Game/login.html'),name='login'),
    url(r'^profile$',views.profile,name='profile'),
    url(r'^logout$',auth_views.LogoutView.as_view(template_name='Game/logout.html'),name='logout'),
    path('admin/', admin.site.urls),

]
