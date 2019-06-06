# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views # Import widoków aplikacji

app_name = 'pizza' # Przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index'),
]