# MCTS


The game of Connect Four is played on a grid with 7 columns and 6 rows, and the basic goal of each player
is to get four of their game pieces in a horizontal, vertical, or diagonal line. Please
see https://en.wikipedia.org/wiki/Connect_Four for more details on the rules and
gameplay. The first part includes implemenation of PCMGS, UR, UCT (and its variations). PMCGS and UR are used only as a baseline, and the UCT algorithm is the focus.

The purpose is to test variations of the UCT algorithm and observe the results.

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

The `human.py` file is a self-contained and runnable file that allows for AI vs human games. <br>

