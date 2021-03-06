# Generated by Django 3.0.6 on 2020-09-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='rating',
            field=models.FloatField(default=3.5),
        ),
        migrations.AlterField(
            model_name='driver',
            name='trips',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='rating',
            field=models.FloatField(default=3.5),
        ),
    ]
