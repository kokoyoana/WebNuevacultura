# Generated by Django 3.0 on 2020-06-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20200626_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoscontacto',
            name='aviso',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='datoscontacto',
            name='cookies',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
