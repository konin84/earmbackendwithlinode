# Generated by Django 4.2.1 on 2023-05-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_service_clientservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='status',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
