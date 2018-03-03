# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pid', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('sort', models.IntegerField(default=0)),
                ('top', models.IntegerField(default=0)),
                ('icon', models.CharField(max_length=256)),
                ('image', models.CharField(max_length=256)),
                ('ascription_type', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
