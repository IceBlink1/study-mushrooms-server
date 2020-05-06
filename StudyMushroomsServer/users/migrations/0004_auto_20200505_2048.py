# Generated by Django 3.0.5 on 2020-05-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200505_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mushroomplace',
            name='location',
        ),
        migrations.AddField(
            model_name='mushroomplace',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='mushroomplace',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]
