# Generated by Django 4.2.5 on 2024-02-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_posts_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='type',
            field=models.CharField(choices=[('competition', 'Competition'), ('post', 'Post'), ('video', 'video'), ('logo', 'Logo')], max_length=150),
        ),
    ]
