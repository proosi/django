# -*- coding: utf-8 -*-
# czat_prj/czat/admin.py

from django.contrib import admin

from czat import models # Importujemy nasz model

# Rejestracja modelu Wiadomosc w panelu administracyjnym
admin.site.register(models.Wiadomosc)
