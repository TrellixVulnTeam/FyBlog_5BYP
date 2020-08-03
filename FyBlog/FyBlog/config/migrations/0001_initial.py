# Generated by Django 2.1.5 on 2019-06-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('href', models.URLField(verbose_name='链接')),
                ('status', models.PositiveIntegerField(choices=[(0, '正常'), (1, '删除')], default=0, verbose_name='状态')),
                ('weight', models.IntegerField(default=10, help_text='权重越高越优先,默认10', verbose_name='权重')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('display_type', models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (3, '最热文章'), (4, '最新评论')], default=1, verbose_name='展示类型')),
                ('content', models.CharField(blank=True, help_text='如果设置的不是HTML类型，可为空', max_length=500, verbose_name='内容')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '侧边栏',
                'verbose_name_plural': '侧边栏',
            },
        ),
    ]
