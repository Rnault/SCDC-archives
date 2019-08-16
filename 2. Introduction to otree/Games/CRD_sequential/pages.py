from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Introduction(Page):
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent

class Contribute1(Page):
    form_model = 'player'
    form_fields = ['contribution1']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution1

class Contribute2(Page):
    form_model = 'player'
    form_fields = ['contribution2']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution2


class Contribute3(Page):
    form_model = 'player'
    form_fields = ['contribution3']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution3

class Contribute4(Page):
    form_model = 'player'
    form_fields = ['contribution4']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution4

class Contribute5(Page):
    form_model = 'player'
    form_fields = ['contribution5']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution5

class Contribute6(Page):
    form_model = 'player'
    form_fields = ['contribution6']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution6

class Contribute7(Page):
    form_model = 'player'
    form_fields = ['contribution7']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution7


class Contribute8(Page):
    form_model = 'player'
    form_fields = ['contribution8']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution8

class Contribute9(Page):
    form_model = 'player'
    form_fields = ['contribution9']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution9

class Contribute10(Page):
    form_model = 'player'
    form_fields = ['contribution10']
    def before_next_page(self):
        group = self.group
        players = group.get_players()
        for p in players:
            p.spent = p.contribution1 + p.contribution2 + p.contribution3 + p.contribution4 + p.contribution5 + p.contribution6 + p.contribution7 + p.contribution8 + p.contribution9 + p.contribution10
            p.moneyLeft = Constants.endowment - p.spent
            p.contribution = p.contribution10

class ResultsWaitPage1(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution1 for p in players]
        group.pot1 = sum(contributions)
        group.contribution_round = group.pot1
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10

class ResultsWaitPage2(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution2 for p in players]
        group.pot2 = sum(contributions)
        group.contribution_round = group.pot2
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10

class ResultsWaitPage3(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution3 for p in players]
        group.pot3 = sum(contributions)
        group.contribution_round = group.pot3
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10

class ResultsWaitPage4(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution4 for p in players]
        group.pot4 = sum(contributions)
        group.contribution_round = group.pot4
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10

class ResultsWaitPage5(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution5 for p in players]
        group.pot5 = sum(contributions)
        group.contribution_round = group.pot5
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10

class ResultsWaitPage6(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution6 for p in players]
        group.pot6 = sum(contributions)
        group.contribution_round = group.pot6
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10

class ResultsWaitPage7(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution7 for p in players]
        group.pot7 = sum(contributions)
        group.contribution_round = group.pot7
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10

class ResultsWaitPage8(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution8 for p in players]
        group.pot8 = sum(contributions)
        group.contribution_round = group.pot8
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10

class ResultsWaitPage9(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution9 for p in players]
        group.pot9 = sum(contributions)
        group.contribution_round = group.pot9
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10

class ResultsWaitPage10(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution10 for p in players]
        group.pot10 = sum(contributions)
        group.contribution_round = group.pot10
        group.total_contribution = group.pot1 + group.pot2 + group.pot3 + group.pot4 + group.pot5 + group.pot6 + group.pot7 + group.pot8 + group.pot9 + group.pot10


class Results(Page):
    #def is_displayed(self):
     #   return self.round_number == Constants.num_rounds
    pass

class FinalCheck(WaitPage):
    def after_all_players_arrive(self):
        if self.group.total_contribution < Constants.target:
            if random.randrange(100) <= Constants.losing:
                self.group.lost = True

class Won(Page):
    def is_displayed(self):
        return self.group.lost == False

class Lost(Page):
    def is_displayed(self):
        return self.group.lost == True

page_sequence = [
    Introduction,
    Contribute1,
    ResultsWaitPage1,
    Results,
    Contribute2,
    ResultsWaitPage2,
    Results,
    Contribute3,
    ResultsWaitPage3,
    Results,
    Contribute4,
    ResultsWaitPage4,
    Results,
    Contribute5,
    ResultsWaitPage5,
    Results,
    Contribute6,
    ResultsWaitPage6,
    Results,
    Contribute7,
    ResultsWaitPage7,
    Results,
    Contribute8,
    ResultsWaitPage8,
    Results,
    Contribute9,
    ResultsWaitPage9,
    Results,
    Contribute10,
    ResultsWaitPage10,
    Results,
    FinalCheck,
    Won,
    Lost
]
