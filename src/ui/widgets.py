import curses
from utils.helpers import formatPercent

def bar(screen, y, x, width, value, max_val, color_pair):
    ratio = max(0, min(value / max_val, 1))
    filled = int(ratio * width)
    bar_str = "=" * filled + "-" * (width - filled)
    screen.draw(y, x, bar_str, curses.color_pair(color_pair))

def label(screen, y, x, text):
    screen.draw(y, x, text)

def box(screen, y, x, h, w):
    top = "+" + "-" * (w - 2) + "+"
    mid = "|" + " " * (w - 2) + "|"
    bot = "+" + "-" * (w - 2) + "+"
    screen.draw(y, x, top)
    for i in range(1, h - 1):
        screen.draw(y + i, x, mid)
    screen.draw(y + h - 1, x, bot)
