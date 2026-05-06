import curses

class Input:
    def __init__(self, game):
        self.game = game

    def handle(self, key):
        if self.game.showMenu:
            self.handleMenu(key)
        elif self.game.finished:
            self.handleFinished(key)
        else:
            self.handleGame(key)

    def handleGame(self, key):
        if key == curses.KEY_UP:
            self.game.increaseHeat()
        elif key == curses.KEY_DOWN:
            self.game.decreaseHeat()
        elif key == ord('r'):
            self.game.rotate()
        elif key == ord('s'):
            self.game.season()
        elif key == ord('t'):
            self.game.takeOut()
        elif key == ord('p'):
            self.game.togglePause()
        elif key == ord('q'):
            self.game.quit()

    def handleMenu(self, key):
        if key == ord('n'):
            self.game.menuNew()
        elif key == ord('l'):
            self.game.menuLoad()
        elif key == ord('q'):
            self.game.quit()

    def handleFinished(self, key):
        if key == ord('q'):
            self.game.quit()
        elif key == ord('n'):
            self.game.reset()
