# Generated by Django 3.0.5 on 2020-07-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_filosofia_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inicio',
            name='iframe1',
        ),
        migrations.RemoveField(
            model_name='inicio',
            name='iframe2',
        ),
        migrations.RemoveField(
            model_name='inicio',
            name='iframe3',
        ),
        migrations.RemoveField(
            model_name='inicio',
            name='iframe4',
        ),
        migrations.AddField(
            model_name='inicio',
            name='fotocuatro',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='inicio',
            name='fotodos',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='inicio',
            name='fotoinicio',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='inicio',
            name='fototres',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
    ]
