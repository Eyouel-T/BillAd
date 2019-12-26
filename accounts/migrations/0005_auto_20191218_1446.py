# Generated by Django 2.2.7 on 2019-12-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_account_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo1', models.ImageField(upload_to='')),
                ('photo2', models.ImageField(upload_to='')),
                ('photo3', models.ImageField(upload_to='')),
                ('photo4', models.ImageField(upload_to='')),
                ('name', models.TextField(max_length=30)),
                ('location', models.TextField(max_length=20)),
                ('rating', models.IntegerField()),
                ('rentStartDate', models.DateField()),
                ('rentEndDate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]