"""eventbrite_api URL Configuration

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
from django.contrib import admin
from eventbrite_api_app.views import event_search_view, EventDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', event_search_view, name='event_search'),
    url(r'^events/(?P<id>\d+)/$', EventDetailView.as_view(), name='event_details'),
]
