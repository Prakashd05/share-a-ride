# Generated by Django 4.2 on 2024-05-22 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_phonenumber_profile_phone_number'),
        ('ride', '0004_alter_ride_user_initiator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='user_initiator',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='user.profile'),
        ),
    ]