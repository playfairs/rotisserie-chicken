import curses

class Screen:
    def __init__(self):
        self.stdscr = None

    def setup(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        self.stdscr.timeout(50)

    def teardown(self):
        if self.stdscr:
            curses.curs_set(1)

    def clear(self):
        self.stdscr.clear()

    def refresh(self):
        self.stdscr.refresh()

    def getch(self):
        return self.stdscr.getch()

    def getMax(self):
        return self.stdscr.getmaxyx()

    def draw(self, y, x, text, attr=0):
        try:
            self.stdscr.addstr(y, x, text, attr)
        except curses.error:
            pass
