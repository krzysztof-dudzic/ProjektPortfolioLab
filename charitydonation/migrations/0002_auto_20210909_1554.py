# Generated by Django 3.1 on 2021-09-09 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitydonation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='pick_up_time',
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_date',
            field=models.DateTimeField(verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.CharField(choices=[('1', 'Fundacja'), ('2', 'Organizacja pozarządowa'), ('3', 'Zbiórka lokalna')], default='1', max_length=2),
        ),
    ]
