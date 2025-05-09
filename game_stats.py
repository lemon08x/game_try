class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        # 任何情况下都不应该重置最高得分
        self.high_score = self._load_high_score()

    def _load_high_score(self):
        """Load the high score from a file."""
        try:
            with open('high_score.txt', 'r') as f:
                return int(f.read().strip())
        except FileNotFoundError:
            return 0
        except ValueError:
            return 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save the high score to a file."""
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))