# Generated by Django 2.2.7 on 2020-01-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('rent', models.CharField(max_length=100)),
            ],
        ),
    ]
