from config import MAX_SEASONING
from utils.helpers import clamp

class Seasoning:
    def __init__(self):
        self.level = 0
        self.applied = 0

    def add(self):
        if self.applied < 10:
            self.level = clamp(self.level + 15, 0, MAX_SEASONING)
            self.applied += 1
            return True
        return False

    def getGrade(self):
        if self.level < 20:
            return "bland"
        elif self.level < 50:
            return "light"
        elif self.level < 80:
            return "perfect"
        else:
            return "over-seasoned"

    def getBonus(self):
        if 50 <= self.level < 80:
            return 1.2
        return 1.0
