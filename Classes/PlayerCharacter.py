from Classes import Character

class PlayerCharacter(Character):
    """Represents the player character. Subclasses Character."""

    def __init__(self, health, attack):
        super().__init__(health, attack)