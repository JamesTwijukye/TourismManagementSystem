# Generated by Django 4.2.11 on 2024-05-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_featureddestination'),
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
