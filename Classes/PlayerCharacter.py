from Classes import Character

class PlayerCharacter(Character):
    """Represents the player character. Subclasses Character."""

    is_dead = False
    experience = 0

    def __init__(self, stats):
        """Initialization method, obviously. Accepts a tuple of ints which are then assigned to the player stats."""
        super().__init__(stats)

    def show_stats(self):
        """Prints player stats on screen."""
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")

    def level_up(self):
        """Increases player level by one."""
        self.level += 1

    def increase_experience(self, amount):
        """Increases player experience by amount."""
        self.experience += amount