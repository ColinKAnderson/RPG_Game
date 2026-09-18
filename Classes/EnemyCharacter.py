from Classes import Character

class EnemyCharacter(Character):
    """Represents an enemy character. Subclasses Character."""

    def __init__(self, level):
        """Initialization method, obviously. Accepts an int to determine enemy level then generates the stats of the
        enemy based on that."""
        self.level = level
        super().__init__(self.generate_stats())

    def generate_stats(self):
        """Generates the stats of the enemy based on its level."""
        return 7,3