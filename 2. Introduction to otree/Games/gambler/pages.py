from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Drawing(Page):
    form_model = 'player'
    form_fields = ['firstChoice']

    def vars_for_template(self):
        return {'b':self.player.nBlueOn8 , 'r': 8 - self.player.nBlueOn8}

class WaitPage1(WaitPage):
    def after_all_players_arrive(self):

        for p in self.group.get_players():
            p.secondChoice = p.firstChoice

class Comparing(Page):

    def vars_for_template(self):
        return {
            'others_choices': [Constants.choices[p.firstChoice-1][1] for p in self.player.get_others_in_group()]
        }

    form_model = 'player'
    form_fields = ['secondChoice']
    def before_next_page(self):
        print(self.player.secondChoice)
        print(self.group.finalDraw)

class WaitPage2(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            if (p.secondChoice == 1 or p.secondChoice == 2) and self.group.finalDraw == 'Blue':
                p.right = True
            elif (p.secondChoice == 3 or p.secondChoice == 4) and self.group.finalDraw == 'Red':
                p.right = True
            else:
                p.right = False


class Test(Page):
    pass

class Ending(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Drawing,
    WaitPage1,
    Comparing,
    WaitPage2,
    Test,
    Ending
]
