# Generated by Django 5.0 on 2024-01-04 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_vendor_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='name',
            field=models.CharField(default='none', max_length=250),
        ),
    ]
