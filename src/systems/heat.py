from config import MAX_HEAT, MIN_HEAT
from utils.helpers import clamp

class Heat:
    def __init__(self):
        self.level = 40

    def increase(self):
        self.level = clamp(self.level + 5, MIN_HEAT, MAX_HEAT)

    def decrease(self):
        self.level = clamp(self.level - 5, MIN_HEAT, MAX_HEAT)
