import time
import curses
from config import TICK_RATE, MAX_BURN
from base.input import Input
from systems.chicken import Chicken
from systems.heat import Heat
from systems.rotation import Rotation
from systems.timer import Timer
from systems.save import Save
from systems.outcome import Outcome
from systems.seasoning import Seasoning
from ui.render import Render

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = False
        self.finished = False
        self.takenOut = False
        self.paused = False
        self.showMenu = False
        self.chicken = Chicken()
        self.heat = Heat()
        self.rotation = Rotation()
        self.timer = Timer()
        self.seasoning = Seasoning()
        self.outcome = None
        self.input_handler = Input(self)
        self.renderer = Render(self)

    def run(self):
        self.running = True
        if self.screen.stdscr is None:
            self.screen.setup(curses.initscr())

        if Save.exists():
            self.showMenu = True
        else:
            Save.delete()

        last_tick = time.time()

        while self.running:
            now = time.time()
            if now - last_tick >= TICK_RATE:
                self.tick()
                last_tick = now

            key = self.screen.getch()
            if key != -1:
                self.input_handler.handle(key)

            self.renderer.draw()

        Save.save(self)
        self.screen.teardown()

    def tick(self):
        if self.finished or self.paused or self.showMenu:
            return

        self.chicken.update(self.heat.level, self.rotation.active)
        self.rotation.update()
        self.timer.tick()

        if self.chicken.burn >= MAX_BURN:
            self.finished = True
            self.outcome = Outcome(self.chicken, self.seasoning)
            self.outcome.evaluate()

    def increaseHeat(self):
        if not self.finished and not self.paused:
            self.heat.increase()

    def decreaseHeat(self):
        if not self.finished and not self.paused:
            self.heat.decrease()

    def rotate(self):
        if not self.finished and not self.paused:
            self.rotation.activate()

    def season(self):
        if not self.finished and not self.paused:
            self.seasoning.add()

    def takeOut(self):
        if self.finished or self.takenOut:
            return
        self.takenOut = True
        self.finished = True
        self.outcome = Outcome(self.chicken, self.seasoning)
        self.outcome.evaluate()

    def togglePause(self):
        if not self.finished:
            self.paused = not self.paused

    def menuNew(self):
        Save.delete()
        self.showMenu = False
        self.reset()

    def menuLoad(self):
        Save.load(self)
        self.showMenu = False

    def reset(self):
        self.chicken = Chicken()
        self.heat = Heat()
        self.rotation = Rotation()
        self.timer = Timer()
        self.seasoning = Seasoning()
        self.finished = False
        self.takenOut = False
        self.paused = False
        self.outcome = None

    def quit(self):
        self.running = False
