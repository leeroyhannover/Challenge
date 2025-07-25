import random

# the gesture
gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# the rules for the game
rules = {
    "Scissors": ["Paper", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Rock": ["Lizard", "Scissors"],
    "Lizard": ["Spock", "Paper"],
    "Spock": ["Scissors", "Rock"]
}

# determine the winner by checking the rules
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Draw"
    elif choice2 in rules[choice1]:
        return "Player 1 wins"
    else:
        return "Player 2 wins"