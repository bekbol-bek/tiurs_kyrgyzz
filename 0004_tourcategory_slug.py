# Generated by Django 5.1 on 2024-08-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_tour_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]