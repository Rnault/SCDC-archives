from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    pid = models.StringField(
        label='What is your full name?'
    )

    age = models.IntegerField(
        label='How old are you?',
        min=13, max=125)

    gender = models.StringField(
        choices=['Male', 'Female', 'Non binary'],
        label='What is your gender?',
        )

    language = models.StringField(
        choices=['english','danish','german','spanish', 'french','italian','other scandinavian', 'other'],
        label="What is your native language?")