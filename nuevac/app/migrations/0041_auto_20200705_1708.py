# Generated by Django 3.0.5 on 2020-07-05 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_auto_20200705_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inicio',
            name='imagen1',
        ),
        migrations.RemoveField(
            model_name='inicio',
            name='imagen2',
        ),
    ]
