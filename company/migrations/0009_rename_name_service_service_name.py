# Generated by Django 4.2.1 on 2023-05-27 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_service_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='service_name',
        ),
    ]
