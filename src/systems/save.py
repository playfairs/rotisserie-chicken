import json
import os
from config import SAVE_FILE

class Save:
    @staticmethod
    def exists():
        return os.path.exists(SAVE_FILE)

    @staticmethod
    def save(game):
        data = {
            "cook": game.chicken.cook,
            "burn": game.chicken.burn,
            "heat": game.heat.level,
            "timer": game.timer.elapsed,
            "taken_out": game.takenOut,
            "seasoning": game.seasoning.level,
            "seasoning_applied": game.seasoning.applied
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load(game):
        if not Save.exists():
            return False
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        game.chicken.cook = data.get("cook", 0)
        game.chicken.burn = data.get("burn", 0)
        game.heat.level = data.get("heat", 40)
        game.timer.elapsed = data.get("timer", 0)
        game.takenOut = data.get("taken_out", False)
        game.seasoning.level = data.get("seasoning", 0)
        game.seasoning.applied = data.get("seasoning_applied", 0)
        return True

    @staticmethod
    def delete():
        if Save.exists():
            os.remove(SAVE_FILE)
