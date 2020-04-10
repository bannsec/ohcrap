
import os, sys
import importlib

class Player:
    """Represents a player at the table."""
    def __init__(self, money, strategy):
        self.money = money
        self.strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy):
        strategy = os.path.abspath(strategy)

        sys.path.append(os.path.dirname(strategy))
        strat = importlib.import_module(os.path.basename(strategy).split(".")[0])

        strat = next(getattr(strat, x) for x in dir(strat) if issubclass(getattr(strat,x), Strategy) and type(getattr(strat,x)) != Strategy)
        self.__strategy = strat(self)

    #
    # Actions the strategy can take
    #

    def pass_line_bet(self, amount):
        if self.money < amount:
            raise OutOfMoney()

        self.money -= amount
        self.table._pass_line_bets[self] = amount

from .exceptions import *
from .strategy import Strategy
