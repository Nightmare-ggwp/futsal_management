# Generated by Django 3.0.8 on 2020-08-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ground', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ground',
            name='description',
        ),
        migrations.AddField(
            model_name='ground',
            name='ground_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='ground',
            name='player_capacity',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='ground',
            name='price',
            field=models.CharField(default='', max_length=10),
        ),
    ]
