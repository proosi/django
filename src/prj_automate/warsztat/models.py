from django.db import models

class Car(models.Model):
    car = models.CharField(max_length=250)
    opis = models.TextField(default='Dodaj opis')

    def __str__(self):
        return self.car

