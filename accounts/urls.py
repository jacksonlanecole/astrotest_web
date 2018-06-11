from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index),
    path('register', views.register, name='register'),
    path('login/', auth_views.login, name='login'),
]
