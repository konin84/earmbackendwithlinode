# Generated by Django 4.2.1 on 2023-05-27 12:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_remove_blogpost_status_blogpost_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name'),
        ),
    ]
