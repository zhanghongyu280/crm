# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-26 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_scorerecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='访谈时间')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Student', verbose_name='学生')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='执行人')),
            ],
        ),
        migrations.AddField(
            model_name='scorerecord',
            name='create_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='积分记录时间'),
        ),
    ]