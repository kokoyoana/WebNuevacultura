# Generated by Django 3.0.5 on 2020-07-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20200705_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradablog',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]