# Generated by Django 4.2.1 on 2023-05-28 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
