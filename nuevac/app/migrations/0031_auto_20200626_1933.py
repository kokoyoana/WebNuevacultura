# Generated by Django 3.0 on 2020-06-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20200626_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inicio',
            name='textinicio',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='inicio',
            name='textoinicio',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
    ]
