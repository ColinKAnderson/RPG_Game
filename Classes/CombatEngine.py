from Classes.EnemyGenerator import EnemyGenerator

class CombatEngine:
    """Utility representing a combat scenario."""

    combat_is_occurring = False
    enemy_group = []
    expected_player_responses = ["attack", "defend","flee"]

    def __init__(self):
        """Initialization method, obviously."""
        pass

    def prepare_combat(self, player):
        """Prepare combat scenario."""
        self.combat_is_occurring = True
        self.enemy_group = EnemyGenerator.generate_enemies(player)
        print("Combat begins!")

    def process_user_input(self, user_input):
        print(f"You {user_input}!")
        if user_input == "attack":
            self.attack()
        elif user_input == "defend":
            self.defend()
        elif user_input == "flee":
            self.flee()

    def attack(self):
        pass

    def defend(self):
        pass

    def flee(self):
        self.combat_is_occurring = False
        print("Combat ends!")
