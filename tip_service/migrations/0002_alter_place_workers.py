# Generated by Django 4.2.1 on 2023-05-26 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tip_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='workers',
            field=models.ManyToManyField(blank=True, related_name='workplace', to='tip_service.worker'),
        ),
    ]
