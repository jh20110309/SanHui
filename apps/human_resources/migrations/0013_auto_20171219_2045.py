# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 20:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0012_auto_20171219_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_name', models.CharField(max_length=20, verbose_name='英文缩写(用于筛选)')),
                ('name', models.CharField(max_length=20, verbose_name='务工地点')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '务工地点',
                'verbose_name_plural': '务工地点',
            },
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='working_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resources.WorkingPlace', verbose_name='务工地点'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='working_salary',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='务工年收入'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='working_years',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='务工年限'),
        ),
    ]
