import random

player1_score = 0
player2_score = 0
winning_score = 5

def flip_coin():
    return random.randint(0, 1)

def player_turn(player, call):
    result = flip_coin()
    if result == call:
        print(f"Player {player} got it right!")
        return True
    else:
        print(f"Player {player} got it wrong.")
        return False

def print_score():
    print(f"Player 1 score: {player1_score}")
    print(f"Player 2 score: {player2_score}")

def check_win():
    if player1_score >= winning_score:
        return 1
    elif player2_score >= winning_score:
        return 2
    else:
        return 0

while True:
    print_score()
    winner = check_win()
    if winner != 0:
        print(f"Player {winner} wins!")
        break
    
    print("Player 1, heads or tails?")