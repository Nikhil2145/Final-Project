#import libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def setup_file():
    """Open history file up if not create and close it"""
    if not os.path.exists("game_history.txt"):
        open("game_history.txt", "w").close()

#creates random number generator for 3 dice with values from 1-6
def roll_dice():
    """Creates dice with random number generator"""
    return list(np.random.randint(1, 7, size = 3))

def is_tuple_out(dice):
    """Checking if tuple out if all values are equal"""
    return dice[0] == dice[1] == dice[2]

def get_fixed_dice(dice):
    """Changes dice to True if equal to each other and returns array"""
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

#starts player turn and gives them results
#prompts the user after if they want to roll again
def take_turn(player_name):
    """rolls dice and gives feedback based off of roll and offers re-roll"""
    print(f"\nIt's {player_name}'s turn!")

    dice = roll_dice()

    print("You rolled: ")

    if is_tuple_out(dice):
        print("Tuple out! You scored 0 this turn.")
        return 0

    fixed = get_fixed_dice(dice)

    while True: 
        for i in range(3): 
            labels = ["FIXED" if f else "FREE" for f in fixed]
            print(f"Die {i + 1}: {dice[i]} ({labels[i]})")
            
        choice = input("Re-roll free dice? (yes/no): ").strip().lower()

        if choice == "no":
            break

        elif choice == "yes":
            for i in range(3):
                if not fixed[i]:
                    dice[i] = np.random.randint(1, 7)

            print("You rolled: " )

            if is_tuple_out(dice):
                print("Tuple out! You scored 0 this turn!")
                return 0
                
            fixed = get_fixed_dice(dice)

        else:
            print("Please enter yes or no.")

    score = sum(dice)
        
    print(f"{player_name} scores {score} points!")

    return score
#creates game history file with winner and player scores
def save_game(winner, player1, score1, player2, score2):
    """Saves game history in a txt file."""

    with open("game_history.txt", "a") as f:
        f.write(
            winner + "," +
            player1 + "," +
            str(score1) + "," +
            player2 + "," +
            str(score2) + "\n"
        )
def show_chart():
    """Show score chart from saved games."""

    data = []

    with open("game_history.txt", "r") as f:

        for line in f:

            parts = line.strip().split(",")

            data.append({
                "player": parts[1],
                "score": int(parts[2])
            })

            data.append({
                "player": parts[3],
                "score": int(parts[4])
            })

    df = pd.DataFrame(data)

    sns.barplot(data=df, x="player", y="score")

    plt.title("Scores Across Games")

    plt.show()

def run_tests():
    """Running tests to make sure triple match is detected and dice get locked"""
    print("Running tests: ")

    # TEST is_tuple_out
    assert is_tuple_out([3, 3, 3]) == True
    assert is_tuple_out([1, 2, 3]) == False
    assert is_tuple_out([5, 5, 4]) == False

    # TEST get_fixed_dice
    assert get_fixed_dice([4, 4, 2]) == [True, True, False]
    assert get_fixed_dice([1, 2, 3]) == [False, False, False]
    assert get_fixed_dice([2, 2, 2]) == [True, True, True]

    print("All tests passed!")
#main function which prompts users for names and begins game
#calculates winner and runs functions to write to CSV file and create chart
def main():
    setup_file()
    print("Welcome to Tuple Out!")
    player1 = input("Enter name for Player 1: ")
    player2 = input("Enter name for Player 2: ")
    print(f"\nOk {player1} and {player2}, let's begin!")

    scores = {player1: 0, player2: 0}

    players = (player1, player2)

    winning_score = 25

    while scores[player1] < winning_score and scores[player2] < winning_score:

        for player in players:

            turn_score = take_turn(player)

            scores[player] = scores[player] + turn_score

            print(f"\nScores: {player1}: {scores[player1]} | {player2}: {scores[player2]}")

            if scores[player] >= winning_score:
                break
    if scores[player1] > scores [player2]:
        winner = player1

    elif scores[player2] > scores [player1]:
        winner = player2

    else:
        winner = "Tie"

    print(f"\nGame Over! {winner} wins!")
    save_game(winner,player1, scores[player1], player2, scores[player2])
    show_chart()
run_tests()   
main()

