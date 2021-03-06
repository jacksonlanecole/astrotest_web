"""astrotest URL Configuration

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
from django.conf.urls import url, include
# IMAGE SERVING IN DEVELOPMENT
from django.conf import settings
from django.conf.urls.static import static

app_url_patterns = [
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('questions/', include('questions.urls')),
    path('exams/', include('exams.urls')),
]

base_url_patterns = [
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^chaining/', include('smart_selects.urls')), # django-smart-selects
]

urlpatterns = app_url_patterns + base_url_patterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


