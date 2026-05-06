class Rotation:
    def __init__(self):
        self.active = False
        self.timer = 0

    def activate(self):
        self.active = True
        self.timer = 10

    def update(self):
        if self.timer > 0:
            self.timer -= 1
            if self.timer <= 0:
                self.active = False
