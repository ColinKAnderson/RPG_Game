import random
from Classes import EnemyCharacter

class EnemyGenerator:
    """Utility to randomly generate enemies based on player level."""

    player_level_to_enemy_group_mapping = {
        1: ( (1,),(1,1) ),
        2: ( (2,),(1,1) ),
        3: ( (3,),(2,1),(1,1,1) )
    }

    def __init__(self, player):
        """Initialization method, obviously. Accepts an int representing the player's level."""
        self.playerLevel = player.level

    def generate_enemies(self):
        """Randomly generates and returns EnemyCharacter objects based on the player's level using the mapping"""
        enemy_group_options = self.player_level_to_enemy_group_mapping[self.playerLevel]
        random_selection = random.randint(0, len(enemy_group_options)-1)
        enemy_group_levels = enemy_group_options[random_selection]
        enemy_group = []
        for selection in enemy_group_levels:
            enemy_group.append(EnemyCharacter(selection))
        return enemy_group