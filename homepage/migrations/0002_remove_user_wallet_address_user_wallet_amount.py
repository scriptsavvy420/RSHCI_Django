# Generated by Django 5.0.4 on 2024-05-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='wallet_address',
        ),
        migrations.AddField(
            model_name='user',
            name='wallet_amount',
            field=models.IntegerField(default=0),
        ),
    ]