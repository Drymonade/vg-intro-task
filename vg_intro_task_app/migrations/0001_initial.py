# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_id', models.CharField(max_length=20)),
                ('machine_model', models.CharField(max_length=20)),
                ('max_load', models.IntegerField()),
                ('current_weight', models.IntegerField()),
            ],
        ),
    ]
