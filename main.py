from models.multi_logic import *

def main():
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    print("Choose game mode:")
    print("1. Single round")
    print("2. Best of three")

    mode = input("Enter 1 or 2: ").strip()
    while mode not in ["1", "2"]:
        mode = input("Invalid input. Please enter 1 or 2: ").strip()

    # Ask user to choose game type (PvC or PvP)
    game_type = input("Choose game type: 'PvC' (Player vs Computer) or 'PvP' (Player vs Player): ").strip()
    while game_type not in ["PvC", "PvP"]:
        game_type = input("Invalid input. Please enter 'PvC' or 'PvP': ").strip()

    # Call corresponding game function
    if mode == "1":
        play_single_game(game_type)   # Single round
    else:
        play_three(game_type)         # Best of three


if __name__ == "__main__":
    main()