"""socialsweethearts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from facebook import views as facebook_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', facebook_views.login),
    url(r'^home/$', facebook_views.home),
    url(r'^logout/$', facebook_views.logout),
    url(r'^deauthorize/$', facebook_views.deauthorize),
    url('', include('social.apps.django_app.urls', namespace='social')),

]
