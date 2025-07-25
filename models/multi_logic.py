import random
from .single_logic import *

# win the 2 from the 3

def play_three(mode='PvC'):
    print('three play, two wins')
    
    player1_wins = 0
    player2_wins = 0
    round_num = 1
    
    while player1_wins < 2 and player2_wins < 2 and round_num <= 3:
        print(f'\n--- Round {round_num}---')
        result = play_single_game(mode)
        
        if result == 'Player 1 wins':
            player1_wins += 1
            
        elif result == 'Player 2 wins':
            player2_wins += 1
            
        else:
            print('Draw for the game. Replay another round')
            continue
            
        round_num += 1
        
    print("\n=== Final Result ===")
    if player1_wins == 2:
        print("Player 1 wins the game!")
    elif player2_wins == 2:
        print("Player 2 wins the game!")
    else:
        print("No clear winner after 3 rounds.")