class Character:
    """Represents characters generally, including the player and enemies."""

    level = 1

    def __init__(self, stats):
        """Initialization method, obviously. Accepts a tuple of ints which are then assigned to character stats."""
        self.health, self.attack = stats

    def decrease_health(self, amount_of_decrease):
        """Decrease the health of the character by amount_of_decrease."""
        self.health -= amount_of_decrease

    def increase_health(self, amount_of_increase):
        """Increase the health of the character by amount_of_increase."""
        self.health += amount_of_increase
