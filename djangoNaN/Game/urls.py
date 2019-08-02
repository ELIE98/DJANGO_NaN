from django.conf.urls import url
from django.urls import path
from . import views
from .views import List_equipe


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register,name='register'),
    url(r'^paris$',views.paris,name='paris'),
    ]
