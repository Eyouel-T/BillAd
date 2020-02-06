# Generated by Django 2.2.7 on 2020-02-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboards', '0005_auto_20200205_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('advertisementType', models.CharField(max_length=200)),
                ('billboard', models.CharField(max_length=200)),
            ],
        ),
    ]
