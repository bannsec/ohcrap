
import logging
import random
from .exceptions import *

class Table:
    """Represents a craps table."""

    def __init__(self, rolls):
        self.players = []

        # Player: Amount bets
        self._pass_line_bets = {}
        self._dont_pass_line_bets = {}

        self._max_rolls = rolls
        self._rolls = 0
        self.come_out = True # Is this a come-out?
        self.point = None # No point yet

    def add_player(self, player):
        player.table = self
        self.players.append(player)

    def _pass_line_winner(self):

        for player, amount in self._pass_line_bets.items():
            # Pay the player
            LOGGER.info("Paying pass line: " + str(amount*2))
            player.money += amount*2 # Pays 1-to-1

            # Notify the player
            player.strategy.on_pass_line_win()

        self._pass_line_bets = {}

    def _pass_line_loser(self):

        for player, amount in self._pass_line_bets.items():
            # Pay the player
            LOGGER.info("Pass line lost: " + str(amount))

            # Notify the player
            player.strategy.on_pass_line_lose()

        self._pass_line_bets = {}

    def _dont_pass_line_winner(self):

        for player, amount in self._dont_pass_line_bets.items():
            # Pay the player
            LOGGER.info("Paying don't pass line: " + str(amount*2))
            player.money += amount*2 # Pays 1-to-1

            # Notify the player
            player.strategy.on_dont_pass_line_win()

        self._dont_pass_line_bets = {}

    def _dont_pass_line_loser(self):

        for player, amount in self._dont_pass_line_bets.items():
            # Pay the player
            LOGGER.info("Don't pass line lost: " + str(amount))

            # Notify the player
            player.strategy.on_dont_pass_line_lose()

        self._dont_pass_line_bets = {}

    def _set_point(self, point):
        self.point = point
        self.come_out = False
        LOGGER.info("Point is: " + str(point))

    def _roll_dice(self):
        """Simply rolls the dice."""
        dice = random.randint(1,6), random.randint(1,6)
        LOGGER.info("Dice rolled: %d, %d", dice[0], dice[1])
        return dice

    def _roll_come_out(self):
        LOGGER.info("Come-out!")
        dice = self._roll_dice()
        total = sum(dice)

        if total in [7, 11]:
            self._pass_line_winner()
            self._dont_pass_line_loser()

        elif total in [2, 3, 12]:
            self._pass_line_loser()

            # 12 is a loss on nopass
            if total in [2, 3]:
                self._dont_pass_line_winner()

        else:
            self._set_point(total)

    def roll(self):
        """Simulates a single roll."""
        self._rolls += 1

        # Notify players
        for player in self.players:
            player.strategy.on_pre_roll(self.come_out)

        if self.come_out:
            self._roll_come_out()

        else:
            self._roll_on()

    def _roll_on(self):
        """Rolling while the game is on."""
        dice = self._roll_dice()
        total = sum(dice)

        if total == self.point:
            self._pass_line_winner()
            self._dont_pass_line_loser()
            self.point = None
            self.come_out = True

        elif total == 7:
            self._pass_line_loser()
            self._dont_pass_line_winner()
            self.point = None
            self.come_out = True

        # TODO: Handle place/put bets here
        # TODO: Handle come/don't come bets here

    def run(self):
        """Runs the simulator to completion."""

        try:
            while self._rolls < self._max_rolls:
                self.roll()
            else:
                print("Out of rolls.")
        except OutOfMoney:
            print("Out of money!")

        # Give players their money back if any is on the table
        # Yes this isn't realistic, but it simplifies things
        for player, bet in self._pass_line_bets.items():
            player.money += bet

        for player, bet in self._dont_pass_line_bets.items():
            player.money += bet

        for player in self.players:
            print("Player money: " + str(player.money))
            print("Average per-roll gain/loss: " + str((player.money - player._starting_money)/self._rolls))

    def __repr__(self):
        return "<Table>"

LOGGER = logging.getLogger(__name__)
