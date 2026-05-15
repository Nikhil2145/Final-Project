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

 Refactored Design: File reading and counting is abstracted into wc_tools.py 
 to make sure of code reusability.

It automatically identifies whether you have given a single file 
or a directory and adjusts its processing.


 ## Validation: 

The code only allows for a one or two-word phrase.

## Key Features

Uses a custom "import" in order to handle large amounts of code.

Generates a wordcount_results.csv file with the search term, location, 
filename, and count for every file that is processed.

Uses try/except blocks and while loops to ensure that the program
doesn't crash if the user enters an invalid path.

Uses dictionaries to store results for easy access.

The count_word_in_file has a tuple with the count and search term used to 
store variables in a single item.


## How to run

Open a terminal and find the project folder, then run:
 python final.py and follow the prompts.

 ## Issues/Bugs

 Words that have punctuation following them such as "bug!" or "bug," would be 
 treated differently.

 Only files in the top-level of the directory are processed, meaning
 subdirectories aren't searched.