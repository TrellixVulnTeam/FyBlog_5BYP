# Generated by Django 2.1.5 on 2019-06-06 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('comment', '0002_auto_20190606_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.Comment'),
        ),
    ]
