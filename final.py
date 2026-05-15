
#import libraries
import numpy as np

#main function which prompts users for names and begins game
def main():
    print("Welcome to Tuple Out!")
    player1 = input("Enter name for Player 1: ")
    player2 = input("Enter name for Player 2: ")
    print(f"\nOk {player1} and {player2}, let's begin!")



#creates random number generator for 3 dice with values from 1-6
def roll_dice():
    return list(np.random.randint(1, 7, size = 3))

def is_tuple_out(dice):
    return dice[0] == dice[1] == dice[2]

def get_fixed_dice(dice):
    
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


def take_turn(player_name):

    print(f"\nIt's {player_name}'s turn!")

    dice = roll_dice()

    print("You rolled: " + str(dice))

    if is_tuple_out(dice):
        print("Tuple out! You scored 0 this turn.")
        return 0

    fixed = get_fixed_dice(dice)

    while True: 

        for i in range(3): 

            label = "FIXED" if fixed[i] else "free"

            print(f"Die {i + 1}: {dice[i]} ({label})")
            
        choice = input("Re-roll free dice? (yes/no): ").strip().lower()

        if choice == "no":
            break

        elif choice == "yes":
            for i in range(3):
                if not fixed[i]:
                    dice[i] = np.random.randint(1, 7)

            print("You rolled: " + str(dice))

            if is_tuple_out(dice):
                print("Tuple out! You scored 0 this turn!")
                return 0
                
            fixed = get_fixed_dice(dice)

        else:
            print("Please enter yes or no.")

    score = sum(dice)
        
    print(f"{player_name} scores {score} points!")

    return score

main()
take_turn("Player 1")