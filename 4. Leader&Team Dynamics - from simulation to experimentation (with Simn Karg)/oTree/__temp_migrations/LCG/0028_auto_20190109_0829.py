# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-09 07:29
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0027_auto_20190109_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='ingame',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]
