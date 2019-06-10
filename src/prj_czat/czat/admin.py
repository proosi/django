# -*- coding: utf-8 -*-
# prj_czat\czat\admin.py

from django.contrib import admin
from .models import Wiadomosc # importuję mój model

admin.site.register(Wiadomosc) # rejestruję mój model

