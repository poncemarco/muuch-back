# Generated by Django 5.1 on 2024-09-01 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_remove_zones_neighborhood'),
        ('users', '0002_address_neighborhood'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Zones',
            new_name='Zone',
        ),
    ]
