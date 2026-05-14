import numpy as np

def main():
    print("Welcome to Tuple Out!")
    player1 = input("Enter name for Player 1: ")
    player2 = input("Enter name for Player 2: ")
    print(f"\nOk {player1} and {player2}, let's begin!")

main()

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

print(roll_dice())


print(is_tuple_out([3, 3, 3]))
print(is_tuple_out([1, 2, 3]))

print(get_fixed_dice([2, 2, 5]))
print(get_fixed_dice([4, 1, 4]))

def take_turn(player_name):

    print(f"\n It's {player_name}'s turn!")

    dice = roll_dice()

    print("You rolled a: " + str(dice))

    if is_tuple_out(dice):
        print("Tuple out! You scored 0 this turn.")
        return 0

        fixed = get_fixed_dice(dice)

        while True: 

            for i in range(3): 

                label = "FIXED" if fixed[i] else "free"

                print(f"Die {i + 1}: {dice[i]} ({label})")
            
            choice = input("Re-roll free dice? (yes/no): ")

            