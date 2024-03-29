# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-04 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('reported_roll_p1', otree.db.models.IntegerField(null=True)),
                ('reported_roll_p2', otree.db.models.IntegerField(null=True)),
                ('checked', otree.db.models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], verbose_name="Do you want to verify the team's report?")),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lcg_group', to='otree.Session')),
            ],
            options={
                'db_table': 'LCG_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('age', otree.db.models.IntegerField(null=True, verbose_name='What is your age?')),
                ('gender', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='What is your gender?')),
                ('q1', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], null=True, verbose_name='I am quick to understand things.')),
                ('q2', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], null=True, verbose_name='whatever mate')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LCG.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lcg_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lcg_player', to='otree.Session')),
            ],
            options={
                'db_table': 'LCG_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lcg_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'LCG_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LCG.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LCG.Subsession'),
        ),
    ]
