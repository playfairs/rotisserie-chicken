import curses
from config import COOK_TARGET, MAX_BURN, MAX_HEAT, MAX_SEASONING, BURN_THRESHOLD, IDEAL_HEAT_LOW, IDEAL_HEAT_HIGH
from ui import widgets

class Render:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.initColors()

    def initColors(self):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def draw(self):
        self.screen.clear()
        h, w = self.screen.getMax()

        if h < 20 or w < 50:
            self.screen.draw(0, 0, "Terminal too small")
            self.screen.refresh()
            return

        if self.game.showMenu:
            self.drawMenu(w, h)
        elif self.game.finished:
            self.drawOutcome(w, h)
        else:
            self.drawGame()

        self.screen.refresh()

    def drawGame(self):
        self.drawHeader(1, 2)
        self.drawTimer(2, 2)
        self.drawHeat(4, 2)
        self.drawCook(7, 2)
        self.drawBurn(10, 2)
        self.drawRotation(13, 2)
        self.drawSeasoning(15, 2)
        self.drawStatus(17, 2)

        if self.game.paused:
            self.drawCenter(50, 18, "PAUSED - Press P to resume", 4)

    def drawMenu(self, w, h):
        self.drawCenter(w, h - 4, "ROTISSERIE CHICKEN", 5)
        self.drawCenter(w, h - 2, "Save found!", 4)
        self.drawCenter(w, h, "N: New Game  |  L: Load Game  |  Q: Quit", 5)

    def drawOutcome(self, w, h):
        out = self.game.outcome
        if not out:
            return

        y = max(2, h // 2 - 6)
        self.drawAt(y, "Results", 5, w)
        self.drawAt(y + 2, f"GRADE: {out.grade}", out.color, w)
        self.drawAt(y + 3, out.message, 5, w)
        self.drawAt(y + 5, f"Cook: {int(self.game.chicken.cook)}%", 5, w)
        self.drawAt(y + 6, f"Burn: {int(self.game.chicken.burn)}%", 5, w)
        self.drawAt(y + 7, f"Seasoning: {out.seasoning_grade}", 4, w)
        self.drawAt(y + 8, f"Time: {self.game.timer.format()}", 5, w)
        self.drawAt(y + 10, "N: New Game  |  Q: Quit", 4, w)

    def drawHeader(self, y, x):
        widgets.label(self.screen, y, x, "ROTISSERIE CHICKEN")

    def drawTimer(self, y, x):
        widgets.label(self.screen, y, x, f"Time:      {self.game.timer.format()}")

    def drawHeat(self, y, x):
        widgets.label(self.screen, y, x, f"Heat:      {int(self.game.heat.level)}%")
        color = 3 if self.game.heat.level > BURN_THRESHOLD else (2 if self.game.heat.level > IDEAL_HEAT_HIGH else 1)
        widgets.bar(self.screen, y + 1, x, 30, self.game.heat.level, MAX_HEAT, color)
        if self.game.heat.level == 0:
            widgets.label(self.screen, y + 2, x, "Is this thing even on?")
        else:
            widgets.label(self.screen, y + 2, x, f"[Ideal: {IDEAL_HEAT_LOW}-{IDEAL_HEAT_HIGH}]")

    def drawCook(self, y, x):
        widgets.label(self.screen, y, x, f"Cook:      {int(self.game.chicken.cook)}%")
        widgets.bar(self.screen, y + 1, x, 30, min(self.game.chicken.cook, COOK_TARGET), COOK_TARGET, 1)

    def drawBurn(self, y, x):
        widgets.label(self.screen, y, x, f"Burn:      {int(self.game.chicken.burn)}%")
        color = 3 if self.game.chicken.burn > 30 else 2
        widgets.bar(self.screen, y + 1, x, 30, self.game.chicken.burn, MAX_BURN, color)

    def drawRotation(self, y, x):
        status = "ACTIVE" if self.game.rotation.active else "IDLE"
        widgets.label(self.screen, y, x, f"Rotation:  {status}")

    def drawSeasoning(self, y, x):
        widgets.label(self.screen, y, x, f"Seasoning: {int(self.game.seasoning.level)}% [{self.game.seasoning.getGrade()}]")
        widgets.bar(self.screen, y + 1, x, 30, self.game.seasoning.level, MAX_SEASONING, 4)

    def drawStatus(self, y, x):
        widgets.label(self.screen, y, x, "UP/DOWN: heat | R: rotate | S: season | T: take out | P: pause | Q: quit")

    def drawCenter(self, w, h, text, color):
        y = h // 2
        x = max(0, (w - len(text)) // 2)
        self.screen.draw(y, x, text, curses.color_pair(color) | curses.A_BOLD)

    def drawAt(self, y, text, color, w):
        x = max(0, (w - len(text)) // 2)
        self.screen.draw(y, x, text.ljust(w - x), curses.color_pair(color))
