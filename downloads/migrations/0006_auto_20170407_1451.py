# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 14:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0005_auto_20170317_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['-date']},
        ),
    ]