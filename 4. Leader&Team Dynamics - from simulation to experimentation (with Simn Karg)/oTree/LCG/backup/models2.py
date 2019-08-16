from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This is the corruption leadership game.....
"""

# The main idea here is to build constants, i.e. what reamins constant during the whole game, and define all other data related stuff (functions, ... that we need)


class Constants(BaseConstants):
    name_in_url = 'Rely_Or_Verify'
    players_per_group = 3
    num_rounds = 20
    instructions_template = 'LCG/Instructions.html'

    show_up_fee = 50

    # Define Equation for payoffs: x = reported number, check: Rely, cheat: team cheated?, ingame = has team lost?
    def PayoffEQ(x,check,cheat,ingame):
        return x - check * x/2 - check * cheat * x/2

    # actual_roll_p1 = 0
    # actual_roll_p2 = 0

class Subsession(BaseSubsession):
    # creating session: what needs to happen every round?
    # - Set random rolls
    def creating_session(self):
        self.session.vars['actual_roll_p1'] = random.randint(1,6)
        self.session.vars['actual_roll_p2'] = random.randint(1,6)
        # print(actual_roll_p1, actual_roll_p2)

    def p1_cheat(self):
        if self.session.vars['actual_roll_p1'] != self.group.reported_roll_p1:
            models.IntegerField(p1_cheat = 1) # has cheated
        else:
            models.IntegerField(p1_cheat = 0)

    def p2_cheat(self):
        if self.session.vars['actual_roll_p2'] != self.group.reported_roll_p2:
            models.IntegerField(p2_cheat = 1) # has cheated
        else:
            models.IntegerField(p2_cheat = 0)

    # determining whether team has cheated
    def team_cheated(self):
        if p1_cheat == 1 or p2_cheat == 1:
            models.IntegerField(team_cheated = 1)
        else:
            models.IntegerField(team_cheated = 0)

    # losegame...? but maybe need to do this differently
    def lose_game(self):
        if group.checked == False and team_cheated == 1 and random.random() <= 0.05:
            ingame = 0


class Group(BaseGroup):
    # setting actual rolls
    # actual_roll_p1 = models.IntegerField(initial = random_roll())
    # actual_roll_p2 = models.IntegerField(initial = random_roll())

    # setting reported rolls
    reported_roll_p1 = models.IntegerField(
        label = "What number did you roll?",
        min=0, max=6,
        doc="""Number reported by P1"""
    )

    reported_roll_p2 = models.IntegerField(
        label = "What number did you roll?",
        min=0, max=6,
        doc="""Number reported by P2"""
    )

    # Leader Decision: Rely or Verify?
    checked = models.BooleanField()

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)

        # All players get the same payoff, depending on whether they cheated or not
        if Group.reported_roll_p1 == Group.reported_roll_p2:
            p1.payoff = p2.payoff = p3.payoff = Constants.PayoffEQ(Group.reported_roll_p1, Group.checked, Subsession.team_cheated)
        else:
            p1.payoff = p2.payoff = p3.payoff = 0

        # Add player payoff
        p1_payment = p1.payoff
        p2_payment = p2.payoff
        p3_payment = p3.payoff


class Player(BasePlayer):
    age = models.IntegerField(
            label='What is your age?',
            min=18, max=90)

    gender = models.StringField(
            choices=['Male', 'Female', 'Other'],
            label='What is your gender?',
            widget=widgets.RadioSelect)

    # For moral personality questionnaire
    def make_field(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7], # 7 point likert scale
            label=label,
            widget=widgets.RadioSelect,
        )

    q1 = make_field('I am quick to understand things.')
    q2 = make_field('whatever mate')
    # q3 = make_field('')
    # q4 = make_field('')

    def role(self):
        return {1: 'Player1', 2: 'Player2', 3: "Leader"}[self.id_in_group]
