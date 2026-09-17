from Classes import *

game = GameObject()
player = PlayerCharacter(10, 5)
enemy = EnemyCharacter(7, 3)

# Run the game loop
while game.is_running:
    player_input = input("> ")

    if player_input.lower() in game.exit_commands:
        game.is_running = False