# Generated by Django 2.1.1 on 2019-10-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(auto_now_add=True, verbose_name='生日'),
        ),
    ]