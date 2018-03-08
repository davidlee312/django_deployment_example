"""learning_users URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from basic_app import views

urlpatterns = [
    # why not call index from basic_app
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),

    #  register and user_login are referenced in basic_app
    url(r'^basic_app/', include('basic_app.urls')),

    # The files below are not under basic_app must be called directly inside the project urls.py
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'special/', views.special, name='special'),

]
