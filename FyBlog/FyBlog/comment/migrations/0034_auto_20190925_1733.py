# Generated by Django 2.1.1 on 2019-09-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0033_auto_20190924_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_parent_id',
            field=models.IntegerField(default=0, verbose_name='上级评论id'),
        ),
    ]