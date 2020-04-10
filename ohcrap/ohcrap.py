
import logging
import argparse

from .player import Player
from .table import Table

def parse_args():
    parser = argparse.ArgumentParser(description='Craps Simulator')
    parser.add_argument("--buyin", "-b", type=int, default=10000,
            help="Amount of money to buy in with (default: 10000)")
    parser.add_argument("--rolls", "-r", type=int, default=100000,
            help="Max rolls to simulate (default: 100000)")
    parser.add_argument("--verbose", "-v", default=False, action="store_true",
            help="Make verbose output.")
    parser.add_argument("strategy", type=str,
            help="Strategy file to play.")

    return parser.parse_args()

def run():
    args = parse_args()

    if args.verbose:
        #logging.getLogger().setLevel(logging.INFO)
        logging.basicConfig(level=logging.INFO)
    
    table = Table(rolls=args.rolls)
    player = Player(money=args.buyin, strategy=args.strategy)

    table.add_player(player)
    table.run()
