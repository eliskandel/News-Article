# Generated by Django 5.0.3 on 2024-03-21 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_rename_publishdate_publisher_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='created_at',
        ),
    ]