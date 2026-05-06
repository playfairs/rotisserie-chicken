from config import COOK_RATE_BASE, BURN_RATE, BURN_THRESHOLD, ROTATION_BONUS, COOK_TARGET, MAX_BURN
from utils.helpers import clamp

class Chicken:
    def __init__(self):
        self.cook = 0
        self.burn = 0
        self.rotation_timer = 0

    def update(self, heat, rotating):
        cook_rate = COOK_RATE_BASE * (heat / 50)

        if rotating:
            cook_rate *= ROTATION_BONUS

        self.cook += cook_rate

        if heat > BURN_THRESHOLD:
            excess = heat - BURN_THRESHOLD
            self.burn += BURN_RATE * (excess / 10)

        if self.cook > COOK_TARGET:
            overcooked = self.cook - COOK_TARGET
            self.burn += 0.05 + (overcooked / 200)

        self.cook = clamp(self.cook, 0, COOK_TARGET * 2)
        self.burn = clamp(self.burn, 0, MAX_BURN)
