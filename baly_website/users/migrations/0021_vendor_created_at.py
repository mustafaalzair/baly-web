# Generated by Django 4.2.5 on 2024-01-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_vendor_main_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
