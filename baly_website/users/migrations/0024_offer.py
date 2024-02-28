# Generated by Django 4.2.5 on 2024-01-27 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_driver_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.vendor')),
            ],
        ),
    ]