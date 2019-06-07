# Generated by Django 2.2.1 on 2019-06-05 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name_plural': 'pizze'},
        ),
        migrations.AlterModelOptions(
            name='skladnik',
            options={'verbose_name_plural': 'składniki'},
        ),
        migrations.AddField(
            model_name='pizza',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]