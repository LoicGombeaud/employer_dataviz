# Generated by Django 5.1.6 on 2025-02-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0005_rename_distance_from_site_cycling_employee_cycling_distance_from_site_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
