# Generated by Django 5.0.4 on 2024-05-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trips", "0004_linkedimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="trip",
            name="trip_price",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]