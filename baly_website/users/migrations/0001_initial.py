# Generated by Django 5.0 on 2023-12-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Captin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=75)),
                ('rating', models.CharField(max_length=50)),
                ('car', models.CharField(max_length=50)),
                ('color_car', models.CharField(max_length=25)),
                ('plate_number', models.CharField(max_length=8)),
                ('phone_number', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vender', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('qr_code', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('lenk', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]