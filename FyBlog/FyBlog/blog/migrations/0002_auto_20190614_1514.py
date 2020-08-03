# Generated by Django 2.1.5 on 2019-06-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='正文必须是markdown格式', verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.TextField(help_text='关于文章的简单描述', verbose_name='摘要'),
        ),
    ]
