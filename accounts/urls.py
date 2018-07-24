from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':
        settings.LOGOUT_REDIRECT_URL}, name='logout'),
    #PASSWORD RESET VIEWS
    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]

