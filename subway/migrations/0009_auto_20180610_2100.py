# Generated by Django 2.0.5 on 2018-06-10 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subway', '0008_auto_20180609_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subwaylandmarkpoint',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subway.Subway'),
        ),
    ]
