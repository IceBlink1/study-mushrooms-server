# Generated by Django 3.0.5 on 2020-05-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200505_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='mushroomplace',
            name='image',
            field=models.TextField(default=''),
        ),
    ]