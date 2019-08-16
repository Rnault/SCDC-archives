from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random as random
import numpy as numpy

author = 'Arnault'

doc = """
Dynamic implementation of the marble gamble task
"""


class Constants(BaseConstants):
    name_in_url = 'marbleGamble'
    players_per_group = 6
    num_rounds = 1
    choices  = [[1, 'Blue Confident'],
             [2, 'Blue Hesitant'],
             [3, 'Red Hesitant'],
             [4, 'Red Confident']]

class Subsession(BaseSubsession):
    def creating_session(self):
        # create a list of pairs to keep track of who played with who
        matrix = self.get_group_matrix()

        # choose distribution randomly for each group(simulate an urn with pb to get blue ball)
        for g in self.get_groups():
            g.pb = random.uniform(0.1, 1)
            g.pr = 1 - g.pb

            # draw for each player
            for p in self.get_players():
                p.nBlueOn8 = 0
                drawing = []
                for i in range(8):
                    a = numpy.random.choice(['Blue', 'Red'], p=[g.pb, g.pr])
                    drawing.append(a)
                for i in drawing:
                    if i == 'Blue':
                        p.nBlueOn8 = p.nBlueOn8 + 1

            # final draw for the whole group
            g.finalDraw = numpy.random.choice(['Blue', 'Red'], p=[g.pb, g.pr])


class Group(BaseGroup):
    pb = models.FloatField()
    pr = models.FloatField()
    finalDraw = models.CharField()


class Player(BasePlayer):

    firstChoice = models.IntegerField(
        choices=Constants.choices,
        widget=widgets.RadioSelect
    )

    secondChoice = models.IntegerField(
        choices=Constants.choices,
        widget=widgets.RadioSelect
    )
    nBlueOn8 = models.IntegerField()
    right = models.BooleanField()

