# Generated by Django 2.1.1 on 2019-10-30 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20191030_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 10, 30, 15, 33, 58, 810298), verbose_name='生日'),
        ),
    ]