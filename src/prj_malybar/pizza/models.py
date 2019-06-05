# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Pizza(models.Model):
    LARGE = 'L'
    MEDIUM = 'm'
    SMALL = 'S'
    ROZMIARY = (
        (LARGE, u'duża'),
        (MEDIUM, u'średnia'),
        (SMALL, u'mała'),
    )
    nazwa = models.CharField(verbose_name='Pizza', max_length=30)
    opis = models.TextField(blank=True, help_text='Opis Pizzy')
    rozmiar = models.CharField(max_length=1, choices=ROZMIARY, default=LARGE)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField('dodano', auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: 
        verbose_name_plural = 'pizze'

    def __unicode__(self):
        return u'%s' % (self.nazwa)

class Skladnik(models.Model):
    pizza = models.ForeignKey(Pizza, 
                              on_delete=models.CASCADE,
                              related_name='skladniki')
    nazwa = models.CharField(verbose_name=u'składniki', max_length=30)
    jarski = models.BooleanField(default=False,
                                  verbose_name='jarski?',
                                  help_text=u'Zaznacz, jeżeli składnik jest odpowiedni dla wegetarian')

    class Meta: 
        verbose_name_plural = u'składniki'

    def __unicode__(self):
        return u'%s' % (self.nazwa)
