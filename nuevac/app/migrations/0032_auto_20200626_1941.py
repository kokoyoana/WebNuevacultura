# Generated by Django 3.0 on 2020-06-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20200626_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inicio',
            name='fotoinicio',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='inicio',
            name='imagenInicio',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
    ]