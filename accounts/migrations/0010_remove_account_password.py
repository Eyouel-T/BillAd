# Generated by Django 2.2.7 on 2020-01-03 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200103_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
    ]
