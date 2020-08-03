# Generated by Django 2.1.1 on 2019-09-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0032_auto_20190913_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='reply_comment',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='reply_user',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_id',
            field=models.IntegerField(default=0, verbose_name='评论id'),
        ),
        migrations.DeleteModel(
            name='reply',
        ),
    ]
