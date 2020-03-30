# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-30 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Swiped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='用户ID')),
                ('sid', models.IntegerField(verbose_name='被滑动的ID')),
                ('stype', models.CharField(choices=[('like', '右滑'), ('superlike', '上滑'), ('dislike', '左滑')], max_length=10, verbose_name='滑动的类型')),
                ('stime', models.DateTimeField(auto_now_add=True, verbose_name='滑动的时间')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='swiped',
            unique_together=set([('uid', 'sid')]),
        ),
    ]
