# Generated by Django 3.1.3 on 2020-11-24 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_delete_somemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='category',
        ),
        migrations.DeleteModel(
            name='Notebook',
        ),
        migrations.DeleteModel(
            name='SmartPhone',
        ),
    ]
