# Generated by Django 4.2 on 2024-06-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0005_alter_ride_user_initiator'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='ride_status',
            field=models.CharField(choices=[('Upcoming', 'Upcoming'), ('Cancelled', 'Cancelled'), (
                'Completed', 'Completed')], default='Upcoming', max_length=10),
        ),
    ]