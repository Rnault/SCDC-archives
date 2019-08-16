"""This defines the pages, i.e. the different stages of the game, what players will see.
The way the game progresses is set by the page_sequence defined at the end.

Rough Draft:
1. Introduction (Consent, ...)
2. Examples
3. Demographics and Moral Character tests..?
4. Player 1 page
5. Player 2 pages
6. Player 3 (leader) page
7. Results page # pages 3-7 get looped.
8. End Results
"""

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1  # only show page at the first round
    pass


class Pre_Questionnaire(Page):
    def is_displayed(self):
        return self.round_number == 1  # only show page at the first round
    form_model = "player"
    form_fields = ["age", "gender"]
    pass


class Examples(Page):
    def is_displayed(self):
        return self.round_number == 1  # only show page at the first round
    pass


class Rolls(WaitPage):
    def after_all_players_arrive(self):
        # self.group.actual_roll_p1 = 3 # for debugging purposes, set dice rolls manually
        # self.group.actual_roll_p2 = 3
        self.group.actual_roll_p1 = random.randint(1, 6)
        self.group.actual_roll_p2 = random.randint(1, 6)
        print(self.group.actual_roll_p1, self.group.actual_roll_p2)
        print([self.subsession.ingame for subsession in self.subsession.in_all_rounds()])


class P1_Roll(Page):
    # This page is only for P1: P1 rolls first die, reports that to P2
    def is_displayed(self):
        return self.player.id_in_group == 1 and all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == True

    form_model = 'group'
    form_fields = ['reported_roll_p1']

    def vars_for_template(self):
        actual_roll_p1 = self.group.actual_roll_p1
        return {"actual_roll_p1": actual_roll_p1,
                # "image_path": "LCG/dice/Dice_{}.JPG".format(self.group.actual_roll_p1)
                "video_path_mp4": "LCG/dice_vids/{}.mp4".format(self.group.actual_roll_p1),
                "video_path_wmv": "LCG/dice_vids/{}.wmv".format(self.group.actual_roll_p1)
                }


class RollWaitPage(WaitPage):
    pass


class P2_Roll(Page):
    """This page is only for P2
    P2 receives information from Player 1
    P2 rolls die
    P2 reports roll to Leader
    """

    def is_displayed(self):
        return self.player.id_in_group == 2 and all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == True

    form_model = 'group'
    form_fields = ['reported_roll_p2']

    def vars_for_template(self):
        reported_roll_p1 = self.group.reported_roll_p1
        actual_roll_p2 = self.group.actual_roll_p2
        return {"reported_roll_p1": reported_roll_p1,
                "actual_roll_p2": actual_roll_p2,
                # "image_path": "LCG/dice/Dice_{}.JPG".format(self.group.actual_roll_p2),
                "video_path_mp4": "LCG/dice_vids/{}.mp4".format(self.group.actual_roll_p2),
                "video_path_wmv": "LCG/dice_vids/{}.wmv".format(self.group.actual_roll_p2)}


class Leader_Page(Page):
    """This page is only for the leader.
    The leader receives the team report and then plays a rely or verify game"""

    def is_displayed(self):
        if self.player.id_in_group == 3 and self.group.reported_roll_p1 == self.group.reported_roll_p2 and all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == True:
            return self
        else:
            return False

    def vars_for_template(self):
        reported_roll_p1 = self.group.reported_roll_p1
        reported_roll_p2 = self.group.reported_roll_p2
        return {"reported_roll_p1": reported_roll_p1, "reported_roll_p2": reported_roll_p2}

    form_model = 'group'
    form_fields = ['checked']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        group = self.group

        if group.reported_roll_p1 != group.actual_roll_p1:
            group.p1_cheat = 1
        else:
            group.p1_cheat = 0

        if group.reported_roll_p2 != group.actual_roll_p2:
            group.p2_cheat = 1
        else:
            group.p2_cheat = 0

        if group.p1_cheat == 1 or group.p2_cheat == 1:
            group.team_cheated = 1
        else:
            group.team_cheated = 0

        if group.checked == False and group.team_cheated == 1 and random.random() <= Constants.LoseGameChance:
            self.subsession.ingame = False
        else:
            self.subsession.ingame = True

        print([self.subsession.ingame for subsession in self.subsession.in_all_rounds()])

        group.set_payoffs()


class Results(Page):
    """This page displays the earnings of each player"""

    def is_displayed(self):
        if all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == True:
            return self
        else:
            return False

    def vars_for_template(self):
        actual_roll_p1 = self.group.actual_roll_p1
        actual_roll_p2 = self.group.actual_roll_p2
        cumulative_payoff = sum(
            [p.payoff for p in self.player.in_all_rounds()])

        return {
            "actual_roll_p1": actual_roll_p1,
            "actual_roll_p2": actual_roll_p2,
            "cumulative_payoff": cumulative_payoff
        }


class LostGame(Page):
    """This page is only shown if a team loses"""

    def is_displayed(self):
        if all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == False:
            return self
        else:
            return False


class FinalEvaluation(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds or all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == False:
            return self
        else:
            return False
    form_model = "group"
    form_fields = []


class PGGInstructions(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds or all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == False:
            return self
        else:
            return False

    def vars_for_template(self):
        cumulative_payoff = sum(
            [p.payoff for p in self.player.in_all_rounds()])
        return {"cumulative_payoff": cumulative_payoff,
                "max_amount": Constants.show_up_fee + cumulative_payoff}


class PGGContribute(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds or all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == False:
            return self
        else:
            return False

    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['contribution']

    # setting dynamic maximum based on endowment and cumulative payoff of previous game
    def contribution_max(self):
        cumulative_payoff = sum(
            [p.payoff for p in self.player.in_all_rounds()])
        return Constants.show_up_fee + cumulative_payoff

    def vars_for_template(self):
        cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])
        return {"max_amount" : Constants.show_up_fee + cumulative_payoff}

    # def contribution_label(self):
    #     cumulative_payoff = sum(
    #         [p.payoff for p in self.player.in_all_rounds()])
    #     max_amount = Constants.show_up_fee + cumulative_payoff
    #     return f"How much will you contribute to the project (from 0 to {max_amount})?"


class PGGResultsWaitPage(WaitPage):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds or all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == False:
            return self
        else:
            return False

    def after_all_players_arrive(self):
        self.group.set_payoffs_PGG()

    body_text = "Waiting for other participants to contribute."


class PGGResults(Page):
    """Players payoff: How much each has earned"""

    def is_displayed(self):
        if self.round_number == Constants.num_rounds or all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == False:
            return self
        else:
            return False

    def vars_for_template(self):
        return {
            'total_earnings': self.group.total_contribution * Constants.multiplier,
        }


class FinalPage(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds or all([self.subsession.ingame for subsession in self.subsession.in_all_rounds()]) == False:
            return self
        else:
            return False


page_sequence = [
    # General Stuff
    Introduction, Pre_Questionnaire,

    # Rely Verify Game
    Examples, Rolls, P1_Roll, RollWaitPage, P2_Roll, RollWaitPage, Leader_Page, ResultsWaitPage, LostGame, Results, FinalEvaluation,

    # PGG
    PGGInstructions, PGGContribute, PGGResultsWaitPage, PGGResults,

    # Finish
    FinalPage]

# Page sequence for debugging
# page_sequence = [Rolls, P1_Roll, RollWaitPage, P2_Roll,
#                  RollWaitPage, Leader_Page, ResultsWaitPage, LostGame, FinalPage]
