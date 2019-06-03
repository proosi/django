"""Definiuje wzorce adresów URL dla learning_logs"""
from django.conf.urls import url

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Strona główna
    url(r'^$', views.index, name='index'),

    # Wyświetlenie wszystkich tematów
    url(r'^topics/$', views.topics, name='topics'),

    # Wyświetlenie wszystkich wpisów.
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Strona przeznaczona do dodawania nowego tematu
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]