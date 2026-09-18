from Classes import Character
import random

class EnemyCharacter(Character):
    """Represents an enemy character. Subclasses Character."""

    stats_table = {
        1: {"health": range(3, 6),
            "attack": range(1, 4)
            },
        2: {"health": range(5, 8),
            "attack": range(3, 7)
            },
        3: {"health": range(7, 10),
            "attack": range(5, 8)
            }
    }

    def __init__(self, level):
        """Initialization method, obviously. Accepts an int to determine enemy level then generates the stats of the
        enemy based on that."""
        self.level = level
        super().__init__(self.generate_stats())

    def generate_stats(self):
        """Generates the stats of the enemy based on its level."""
        stat_ranges = self.stats_table[self.level]
        health = random.choice(stat_ranges["health"])
        attack = random.choice(stat_ranges["attack"])
        return health,attack
