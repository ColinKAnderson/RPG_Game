from Classes import *

# Create required objects
game = GameObject()
player = PlayerCharacter((10, 5))
combat_engine = CombatEngine()

# Run the game loop
while game.is_running:
    user_input = (input("> ")).lower()

    if user_input in game.exit_commands:
        game.is_running = False
    elif combat_engine.combat_is_occurring:
        if user_input in combat_engine.expected_player_responses:
            combat_engine.process_user_input(user_input)
    elif user_input == "fight":
        combat_engine.prepare_combat(player)

    if player.is_dead:
        print("You lose!")
        game.is_running = False
