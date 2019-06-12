# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Car

def index(request):
    """Strona główna"""
    cars = Car.objects.order_by('car')
    print(cars)
    for car in cars:
        print(car)
    kontekst = {'cars': cars }
    return render(request, 'warsztat/index.html', kontekst)
