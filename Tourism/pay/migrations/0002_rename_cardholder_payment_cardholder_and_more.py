# Generated by Django 4.2.11 on 2024-04-20 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='cardHolder',
            new_name='cardholder',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='total',
            new_name='price',
        ),
    ]
