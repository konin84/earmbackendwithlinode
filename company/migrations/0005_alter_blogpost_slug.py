# Generated by Django 4.2.1 on 2023-05-20 22:34

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
