# Generated by Django 2.2.13 on 2020-06-22 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20200622_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='videofile',
        ),
    ]
