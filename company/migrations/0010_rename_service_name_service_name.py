# Generated by Django 4.2.1 on 2023-05-27 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_rename_name_service_service_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_name',
            new_name='name',
        ),
    ]
