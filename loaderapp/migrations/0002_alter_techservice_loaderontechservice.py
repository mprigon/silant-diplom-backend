# Generated by Django 4.2.3 on 2023-07-26 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loaderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techservice',
            name='loaderOnTechService',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loaderapp.loader'),
        ),
    ]
