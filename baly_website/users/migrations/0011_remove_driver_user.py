# Generated by Django 5.0 on 2024-01-05 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_vendor_user_driver_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='user',
        ),
    ]
