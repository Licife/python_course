class GameStats:
    def __init__(self, ai_game):
        self.score = None
        self.ships_left = None
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
