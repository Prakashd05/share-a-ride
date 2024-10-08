# Generated by Django 4.2 on 2024-06-27 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_user'),
        ('ride', '0006_ride_ride_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='co_passengers',
            field=models.ManyToManyField(
                related_name='co_passengers', to='user.profile'),
        ),
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('request_status', models.CharField(choices=[('Accepted', 'Accepted'), (
                    'Rejected', 'Rejected'), ('Pending', 'Pending')],
                    default='Pending', max_length=10)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                 related_name='copassenger', to='ride.ride')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                 related_name='copassenger', to='user.profile')),
            ],
        ),
    ]
