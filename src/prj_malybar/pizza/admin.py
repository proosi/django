# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models

# Rejestrujemy modele w panelu administracyjnym
admin.site.register(models.Pizza)
admin.site.register(models.Skladnik)
