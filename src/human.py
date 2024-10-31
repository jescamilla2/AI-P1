import random
import math
from algorithms import uniform_random_move
from algorithms import pmcgs_move
from algorithms import uct_move
from connect_four import ConnectFour
from node import Node
from tree import Tree

def ai_move(game, algorithm='UR'):
    """Generates a valid move for the AI based on the chosen algorithm."""
    if algorithm == "UR":
        return uniform_random_move(game)
    elif algorithm == "PMCGS":
        return pmcgs(game, 100)
    elif algorithm == "UCT":
        return uct_move(game, 100)
    else:
        raise ValueError(f"Unknown AI algorithm: {algorithm}")

def human_move(game):
    """Prompts the human player for a valid move."""
    while True:
        try:
            col = int(input(f"Player {game.current_player}, choose a column (0-6): "))
            if col in game.valid_moves:
                return col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a valid integer between 0 and 6.")

def play_game(algorithm):
    """Simulates a game of Connect Four between an AI and a human player."""
    game = ConnectFour()
    game.display_board()

    while not game.game_over:
        if game.current_player == 'R':  # Human player
            move = human_move(game)
            print(f"Player {game.current_player} chooses column {move}.")
        else:  # AI player
            move = ai_move(game, algorithm)
            print(f"AI chooses column {move}.")

        game.make_move(move)
        game.display_board()  # Optionally display the board after each move

    if game.winner:
        print(f"Player {game.winner} wins!")
    elif game.draw:
        print("It's a draw!")


if __name__ == '__main__':
    # Start the game
    play_game('UCT')
