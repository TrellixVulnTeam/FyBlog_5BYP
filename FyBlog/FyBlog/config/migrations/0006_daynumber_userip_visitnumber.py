# Generated by Django 2.1.1 on 2019-10-15 21:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20190722_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('count', models.IntegerField(default=0, verbose_name='网站访问次数')),
            ],
            options={
                'verbose_name': '网站日访问统计',
                'verbose_name_plural': '网站日访问统计',
            },
        ),
        migrations.CreateModel(
            name='Userip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='ip地址')),
                ('count', models.IntegerField(default=0, verbose_name='访问次数')),
            ],
            options={
                'verbose_name': '访问用户信息',
                'verbose_name_plural': '访问用户信息',
            },
        ),
        migrations.CreateModel(
            name='VisitNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='网站访问总次数')),
            ],
            options={
                'verbose_name': '网站访问总次数',
                'verbose_name_plural': '网站访问总次数',
            },
        ),
    ]
