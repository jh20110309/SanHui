# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 19:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0011_auto_20171218_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeOfEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_name', models.CharField(max_length=20, verbose_name='英文缩写(用于筛选)')),
                ('name', models.CharField(max_length=20, verbose_name='文化程度')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '文化程度',
                'verbose_name_plural': '文化程度',
            },
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='degree_of_education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resources.DegreeOfEducation', verbose_name='文化程度'),
        ),
    ]
