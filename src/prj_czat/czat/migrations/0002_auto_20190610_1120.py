# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-10 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('czat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wiadomosc',
            options={'ordering': ['data_pub'], 'verbose_name': 'wiadomość', 'verbose_name_plural': 'wiadomości'},
        ),
    ]
