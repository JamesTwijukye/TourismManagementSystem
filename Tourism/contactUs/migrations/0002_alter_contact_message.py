# Generated by Django 4.2.11 on 2024-04-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactUs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=200),
        ),
    ]