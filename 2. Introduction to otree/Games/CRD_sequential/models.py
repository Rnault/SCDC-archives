from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'CRD'
    players_per_group = 2

    endowment = 40
    target = int((players_per_group/2)*endowment)
    losing = 90
    num_rounds = 1
    instructions_template = 'CRD_sequential/Instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
        else:
            self.group_like_round(1)


class Group(BaseGroup):
    pot1 = models.IntegerField(initial=0)
    pot2 = models.IntegerField(initial=0)
    pot3 = models.IntegerField(initial=0)
    pot4 = models.IntegerField(initial=0)
    pot5 = models.IntegerField(initial=0)
    pot6 = models.IntegerField(initial=0)
    pot7 = models.IntegerField(initial=0)
    pot8 = models.IntegerField(initial=0)
    pot9 = models.IntegerField(initial=0)
    pot10 = models.IntegerField(initial=0)

    contribution_round = models.IntegerField(initial=0)
    total_contribution = models.IntegerField(initial=0)
    lost = models.BooleanField(initial=False)

class Player(BasePlayer):
    moneyLeft = models.IntegerField(initial=0)
    spent = models.IntegerField(initial=0)
    sumContribution = models.IntegerField(initial=0)
    contribution = models.IntegerField(initial=0)

    contribution1 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )

    contribution2 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )

    contribution3 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )

    contribution4 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )

    contribution5 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )

    contribution6 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )

    contribution7 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )

    contribution8 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )

    contribution9 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )

    contribution10 = models.IntegerField(
        min=0, max=Constants.endowment, initial=0,
        label="How much will you contribute?"
    )