from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1


class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplier

        return {
                'tripled_amount': tripled_amount,
                'prompt': 'Please an amount from 0 to {}'.format(tripled_amount)}

    def sent_back_amount_max(self):
        return self.group.sent_amount * Constants.multiplier


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

#class ShuffleWaitPage(WaitPage):
#    after_all_players_arrive = True
#    def after_all_players_arrive(self):
#        self.subsession.group_randomly()


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplier,
            'payoff_A': self.group.sent_amount * Constants.multiplier-self.group.sent_back_amount,
            'payoff_B': Constants.endowment - self.group.sent_amount + self.group.sent_back_amount
        }


page_sequence = [
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
    #ShuffleWaitPage,
]