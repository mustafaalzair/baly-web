# Generated by Django 4.2.5 on 2024-01-21 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_driver_password_alter_vendor_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='lenk',
            new_name='link',
        ),
    ]
