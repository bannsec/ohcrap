
"""
Strategy: Basic Pass
Description: This strategy simply bets on the pass line over and over. No
    changes in bets and no odds.
"""

from ohcrap.strategy import Strategy

class BasicPass(Strategy):
    def on_pre_roll(self, come_out):

        # Only betting on come-out
        if come_out:
            # Bet strait 5
            self.player.pass_line_bet(5)

