
import logging

class Strategy:
    def __init__(self, player):
        self.player = player

    ###########
    # Actions #
    ###########

    # Implement these only if interested in knowing when things have happened.
    def on_pre_roll(self, come_out):
        """This is called before EVERY roll.
        
        Args:
            come_out (bool): Is this a come-out roll?

        This is your main point to make your bets for the roll.
        """
        pass

    def on_pass_line_win(self): pass
    def on_pass_line_lose(self): pass
    def on_dont_pass_line_win(self): pass
    def on_dont_pass_line_lose(self): pass


LOGGER = logging.getLogger(__name__)
