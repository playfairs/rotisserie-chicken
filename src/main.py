import curses
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from base.screen import Screen
from base.game import Game

def main(stdscr=None):
    screen = Screen()
    if stdscr:
        screen.setup(stdscr)
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    curses.wrapper(main)
