"""API URL Configuration

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
from dibe import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API DOCUMENT')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^share/$', views.ShareRideList().as_view(), name='share-ride-list'),
    url(r'^host/$', views.HostRideList().as_view(), name='host-ride-list'),
    url(r'^login', views.UserLogin.as_view()),
    url(r'^api-doc', schema_view),
]
