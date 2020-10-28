# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-21 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='跟进内容')),
                ('date', models.DateField(auto_now_add=True, verbose_name='跟进日期')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='跟踪人')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Customer', verbose_name='所咨询客户')),
            ],
        ),
    ]