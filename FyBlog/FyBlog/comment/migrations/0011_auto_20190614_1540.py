# Generated by Django 2.1.5 on 2019-06-14 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0010_auto_20190614_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='reply_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.Comment'),
        ),
    ]