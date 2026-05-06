from config import RAW_MAX, RARE_MAX, PERFECT_MIN, PERFECT_MAX, OVERCOOKED_MAX, COOK_TARGET, MAX_BURN

class Outcome:
    def __init__(self, chicken, seasoning):
        self.chicken = chicken
        self.seasoning = seasoning
        self.grade = None
        self.message = None
        self.color = None
        self.seasoning_grade = None

    def evaluate(self):
        cook = self.chicken.cook
        burn = self.chicken.burn

        if burn >= MAX_BURN * 0.9:
            self.grade = "CHARCOAL"
            self.message = "It's pure carbon now."
            self.color = 3
        elif cook < RAW_MAX:
            self.grade = "RAW"
            self.message = "Still clucking. Unsafe to eat."
            self.color = 4
        elif cook < RARE_MAX:
            self.grade = "RARE"
            self.message = "Pink inside. Not quite there."
            self.color = 2
        elif PERFECT_MIN <= cook <= PERFECT_MAX and burn < 20:
            self.grade = "PERFECT"
            self.message = "Golden, juicy, flawless!"
            self.color = 1
        elif cook <= OVERCOOKED_MAX:
            if burn > 40:
                self.grade = "BURNT"
                self.message = "Crispy on the outside, dry inside."
                self.color = 3
            else:
                self.grade = "WELL DONE"
                self.message = "A bit dry but edible."
                self.color = 2
        else:
            self.grade = "OVERCOOKED"
            self.message = "Tough as leather."
            self.color = 3

        self.seasoning_grade = self.seasoning.getGrade()
        return self.grade
