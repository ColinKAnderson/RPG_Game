from Classes import *

# Create required objects
game = GameObject()
player = PlayerCharacter((10, 5))
enemy_generator = EnemyGenerator(player)

# Run the game loop
while game.is_running:
    user_input = input("> ")

    if user_input.lower() in game.exit_commands:
        game.is_running = False