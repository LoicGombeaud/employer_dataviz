# Generated by Django 5.1.6 on 2025-02-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0003_alter_territoryliaison_territory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='distance_from_site_cycling',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='distance_from_site_direct',
            field=models.IntegerField(null=True),
        ),
    ]
