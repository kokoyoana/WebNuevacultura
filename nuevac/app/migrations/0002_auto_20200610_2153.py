# Generated by Django 2.2.12 on 2020-06-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociacion',
            name='textoAsociacion',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]