# Generated by Django 2.0.5 on 2018-06-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subway', '0009_auto_20180610_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='subwaylandmarkpoint',
            name='landmark_name',
            field=models.CharField(default='Not-Set-Landmark', max_length=50),
        ),
    ]
