# Generated by Django 4.2.5 on 2024-01-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_vendor_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='Main_Category',
            field=models.CharField(default='', max_length=120),
        ),
    ]