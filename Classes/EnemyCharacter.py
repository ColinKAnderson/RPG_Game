from Classes import Character

class EnemyCharacter(Character):
    """Represents an enemy character. Subclasses Character."""

    def __init__(self, health, attack):
        super().__init__(health, attack)