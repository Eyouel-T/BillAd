# Generated by Django 2.2.7 on 2019-12-18 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191218_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phoneNumber',
        ),
    ]