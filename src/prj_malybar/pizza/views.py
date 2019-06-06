# -*- coding: utf-8 -*-

from django.shortcuts import render

def index(request):
    u"""Strona główna"""
    kontekst = { 'komunikat': 'Witaj w aplikacji Pizza!'}
    return render(request, 'pizza/index.html', kontekst)

