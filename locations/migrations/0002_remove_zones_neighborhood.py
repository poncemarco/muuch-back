# Generated by Django 4.1.6 on 2024-04-20 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zones',
            name='neighborhood',
        ),
    ]