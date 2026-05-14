import numpy as np

def main():
    print("Welcome to Tuple Out!")
    player1 = input("Enter name for Player 1: ")
    player2 = input("Enter name for Player 2: ")
    print(f"\nOk {player1} and {player2}, let's begin!")

main()

def roll_dice():
    return list(np.random.randint(1, 7, size = 3))

def is_tuple_out():
    return dice[0] == dice[1] == dice[2]

def get_fixed_dice():
    
    fixed = [False, False, False]

    if dice[0] == dice[1]:
        fixed[0] = True
        fixed[1] = True

    if dice[0] == dice[2]:
        fixed[0] = True
        fixed[2] = True

    if dice[1] == dice[2]:
        fixed[1] = True
        fixed[2] = True
    
    return fixed

print(roll_dice())

dice = roll_dice()