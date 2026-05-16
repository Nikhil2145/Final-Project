# Project Name
Tuple Out

Tuple Out is a Python program that is played between two people.
Each player has a turn to roll three dice and if they all match, 
the player gets a Tuple Out and scores 0 for their turn. If they
don't all match, players can re-roll the dice to improve score.
Every player's turn is added to the score and the first player to 25 wins.
The game results are saved to a txt file and a graph with player scores is made.

## Prerequisites

Python is needed to run this program. The libraries are also needed for this program.
You can install them by writing in terminal: 
pip install numpy pandas matplotlib seaborn

The file is ran in final.py and it prompts the users for their names.

 ## Key logic:

The game loops between two players until one player reaches 25 points.

For each turn:
three dice are rolled and matching dice are FIXED
the player may continue to roll free dice until they want to stop
or it matches other fixed dice.

Game results are saved after the match and is turned into a graph
displaying scores across games 

 ## Validation: 

The code only allows for a yes or no response when asked to reroll.
Invalid responses prompts the user to respond again.

## Key Features

Uses a random number generator to simulate three 6-faced dice being rolled.

Generates a game_history.txt file if it does not exist and adds
winner and player names and scores. Reads the saved data for graphing

Data visualization: uses pandas, seaborn, matplotlib
to generate a bar graph showing players and their scores across games.

Uses dictionaries to store results for easy access and track player's scores
throughout the game.

Automated testing through assert statements to check
Tuple Out detection and fixed dice logic.

Fixed dice system where dice that match up become locked
and aren't able to be rolled again for the user's turn.


## How to run

Open a terminal and find the project folder, then run:
 python final.py and follow the prompts.

 ## Issues/Bugs

Very large game_history text files will be crowded and hard to decipher.

