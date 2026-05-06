class Timer:
    def __init__(self):
        self.elapsed = 0

    def tick(self):
        self.elapsed += 1

    def reset(self):
        self.elapsed = 0

    def format(self):
        mins = self.elapsed // 600
        secs = (self.elapsed % 600) // 10
        return f"{mins}:{secs:02d}"
