# Generated by Django 4.2 on 2024-01-16 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemorder',
            old_name='item',
            new_name='items',
        ),
        migrations.CreateModel(
            name='RequestItemOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField()),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.requestitem')),
            ],
        ),
    ]
