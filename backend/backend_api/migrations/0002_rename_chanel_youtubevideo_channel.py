# Generated by Django 5.0.2 on 2024-03-03 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtubevideo',
            old_name='chanel',
            new_name='channel',
        ),
    ]
