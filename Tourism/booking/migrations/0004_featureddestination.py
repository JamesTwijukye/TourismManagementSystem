# Generated by Django 4.2.11 on 2024-05-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_hotel_id_alter_booking_personal_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_id', models.CharField(max_length=230)),
                ('dest_text', models.CharField(max_length=530)),
                ('dest_tittle', models.CharField(max_length=530)),
                ('dest_image', models.ImageField(upload_to='dest_images')),
            ],
        ),
    ]