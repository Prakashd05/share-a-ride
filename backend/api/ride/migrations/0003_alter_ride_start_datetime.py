# Generated by Django 4.2 on 2024-05-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0002_alter_ride_start_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='start_datetime',
            field=models.DateTimeField(),
        ),
    ]
