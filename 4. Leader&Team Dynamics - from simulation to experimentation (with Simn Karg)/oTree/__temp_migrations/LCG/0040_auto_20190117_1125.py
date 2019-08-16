# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-17 10:25
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('LCG', '0039_auto_20190117_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='q1',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='I try hard to act honestly in most things I do.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q10',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='It is ok to do something you know is wrong if the rewards for doing it are great.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q11',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='If no one is watching or will know it does not matter if I do the right thing.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q12',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='It is more important that people think you are honest than being honest.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q13',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='If no one could find out, it is okay to steal a small amount of money or other things that no one will miss.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q14',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='There is no point in going out of my way to do something good if no one is around to appreciate it.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q15',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='If a cashier accidentally gives me kr 10 extra change, I usually act as if I did not notice it.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q16',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='Lying and cheating are just things you have to do in this world. '),
        ),
        migrations.AlterField(
            model_name='player',
            name='q17',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='Doing things that some people might view as not honest does not bother me.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q18',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='If people treat me badly, I will treat them in the same manner.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q19',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='I will go along with a group decision, even if I know it is morally wrong.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q2',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='Not hurting other people is one of the rules I live by.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q20',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name="Having moral values is worthless in today's society."),
        ),
        migrations.AlterField(
            model_name='player',
            name='q3',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='It is important for me to treat other people fairly.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q4',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='I want other people to know they can rely on me.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q5',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='I always act in ways that do the most good and least harm to other people.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q6',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='If doing something will hurt another person, I try to avoid it even if no one would know.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q7',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='One of the most important things in life is to do what you know is right.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q8',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='Once I′ve made up my mind about what is the right thing to do, I make sure I do it.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q9',
            field=otree.db.models.IntegerField(choices=[[1, 'strongly agree'], [2, "don't agree"]], null=True, verbose_name='As long as I make a decision to do something that helps me, it does not matter much if other people are harmed.'),
        ),
    ]
