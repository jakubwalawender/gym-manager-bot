# Generated by Django 4.0.4 on 2022-05-27 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_alter_location_address_alter_location_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='possiblereservation',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservations.location'),
            preserve_default=False,
        ),
    ]
