#!/usr/bin/env Python3

from brain_games.engine import get_inputs
from brain_games.games import calc_game

def main():
    get_inputs(calc_game)


if __name__ == '__main__':
    main()
