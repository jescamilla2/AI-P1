# Game Playing Agents


In this assignment you will be developing AI agents to play the game of Connect
Four based on the MCTS approach we have discussed in class. The game of Connect
Four is played on a grid with 7 columns and 6 rows, and the basic goal of each player
is to get four of their game pieces in a horizontal, vertical, or diagonal line. Please
see https://en.wikipedia.org/wiki/Connect_Four for more details on the rules and
gameplay. In the first part you will develop and test algorithms for making move
selections given a specific board state. In the second part you will test these
algorithms against each other in actual game play.

## Part 1:

Usage is straightforward. To run one of the algorithms, use of the CLI is required. 
From the `src` folder, run the following:

`$ python ./main.py filename.txt print_option sims`

where

 - `filename.txt` is the path to the input file that contains the current game state and algorithm
 - `print_option` can be Verbose, Brief, or None to control what gets printed as the algorithm runs
 - `sims` is the total number of simulations to run as nodes are explored


## Part 2:

The `tournament.py` file is a self-contained executable. Simply run the main method to see the tournament results
Adjustments can be made to the algorithms' specifications.

## Part 3:

a. The `human.py` file is a self-contained and runnable file that allows for AI vs human games. <br>
b. The modified UCT algorithm is located in the `algorithms.py` file.
