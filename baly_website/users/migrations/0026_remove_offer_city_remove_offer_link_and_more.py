# Generated by Django 4.2.5 on 2024-01-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_offer_city_offer_link_offer_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='link',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='offer',
            name='Platinum',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='offer',
            name='Silver',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='offer',
            name='golden',
            field=models.TextField(default=''),
        ),
    ]
