# Generated by Django 3.0.5 on 2020-07-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_delete_tallere'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tallere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(blank=True, max_length=5000, null=True)),
                ('taller', models.TextField(blank=True, max_length=5000, null=True)),
                ('imagentalleres', models.ImageField(blank=True, upload_to='static/img')),
            ],
        ),
    ]
