# Generated by Django 4.2.11 on 2024-05-03 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_rename_itembutton_trips_trip_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trips',
            new_name='Trip',
        ),
    ]