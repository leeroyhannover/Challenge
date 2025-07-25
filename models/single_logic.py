import random
from .rules import *

# main func for the game
def play_single_game(mode="PvC"):
    print("Available gestures: Rock, Paper, Scissors, Lizard, Spock")

    if mode == "PvC":
        player_choice = input("Player, enter your choice: ").capitalize()
        while player_choice not in gestures:
            player_choice = input("Invalid choice. Try again: ").capitalize()

        computer_choice = random.choice(gestures)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)
        return result

    elif mode == "PvP":
        player1_choice = input("Player 1, enter your choice: ").capitalize()
        while player1_choice not in gestures:
            player1_choice = input("Invalid choice. Try again: ").capitalize()

        player2_choice = input("Player 2, enter your choice: ").capitalize()
        while player2_choice not in gestures:
            player2_choice = input("Invalid choice. Try again: ").capitalize()

        result = determine_winner(player1_choice, player2_choice)
        print(result)
        return result

    else:
        print("Invalid mode. Use 'PvC' or 'PvP'.")
        return None