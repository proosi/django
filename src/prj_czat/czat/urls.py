# -*- coding: utf-8 -*-
# czat/urls.py

from django.conf.urls import url
from . import views # Import widoków aplikacji

app_name = 'czat' # Przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index')
]