# Generated by Django 4.2.11 on 2024-05-14 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0003_rename_services_payment_number_of_rooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='number_of_rooms',
            new_name='services',
        ),
    ]
