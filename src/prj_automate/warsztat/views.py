# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    """Strona główna"""
    kontekst = { 'komunikat': 'Witaj w aplikacji Warsztat!'}
    return render(request, 'warsztat/index.html', kontekst)
