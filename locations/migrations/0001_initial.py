# Generated by Django 4.2 on 2024-03-17 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zones', to='locations.neighborhood')),
            ],
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighborhoods', to='locations.zones'),
        ),
    ]
