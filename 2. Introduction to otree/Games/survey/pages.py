from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['pid','age',
                   'gender','language']


page_sequence = [
    Intro,
    Demographics
]
