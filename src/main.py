from algorithms import uniform_random_move
from algorithms import pmcgs_move
from algorithms import uct_move
import connect_four as c4
import argparse

def extract_board(file_path):
    """extract the game contents from the game file"""
    with open(file_path, 'r') as file:
        algorithm = file.readline().strip()  # First line is the algorithm
        current_player = file.readline().strip()  # Second line is the player making the next move
        board = [list(file.readline().strip()) for _ in range(6)]  # Next six lines are the board rows

    return algorithm, current_player, board



def best_move(game, algorithm=None, simulations=0, print_out='None'):
    """input is a connect_four game board and the algorithm to use to determine the next best move"""

    if algorithm == 'UR':
        # perform uniform random move
        if(print_out=='Verbose' or print_out=='Brief'):
            move = uniform_random_move(game, print_out=True)
        else:
            move = uniform_random_move(game)
    elif algorithm == 'PMCGS':
        # perform a moved based on Pure Monte Carlo Game Search
        move = pmcgs_move(game, simulations, print_out)

    elif algorithm == 'UCT':
        # perform a move based Upper Confidence bound for Trees
        move = uct_move(game, simulations, print_out)
    else:
        print('No algorithm selected. Please select.')

    return move

def main():
    '''
    :param: None
    :return: Nothing.
    '''

    # create a parser object
    parser = argparse.ArgumentParser('Connect Four', description='Connect Four game')

    # add the arguments
    parser.add_argument('filepath', type=str, help='file containing the game')
    parser.add_argument('print_output', type=str, nargs='?', default="None",
                        choices=['Verbose', 'Brief', 'None'],
                        help='controls what the algorithm will print for output')
    parser.add_argument('simulations', type=int, help='the number of simulations to run')

    # parse the arguments
    args = parser.parse_args()

    # get the board, current_player, and algorithm
    algorithm, current_player, board = extract_board(args.filepath)

    # create the board, load the current state, and display
    game = c4.ConnectFour()
    game.load_board(board, current_player)


    if (args.print_output=='Verbose' or args.print_output=='Brief'):
        print('Below is the current state of the game.')
        print(f'It is {"Red" if current_player == "R" else "Yellow"} player\'s turn')
        game.display_board()


    # compute the next move based on the algorithm; print if option entered
    best_move(game, algorithm, args.simulations, args.print_output)






if __name__ == '__main__':
    # execute only if run as a script
    main()




"""
# Example usage:
if __name__ == "__main__":
    game = ConnectFour()
    game.play()
"""
