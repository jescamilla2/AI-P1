from algorithms import uniform_random_move
from algorithms import pmcgs
from algorithms import uct_move
import connect_four as c4





"""
def main():
    '''
    :param: None
    :return: Nothing. Just prints out the path as well as a simple diagram.
    '''

    # create a parser object
    parser = argparse.ArgumentParser('Connect Four', description='Connect Four game')

    # add the arguments
    parser.add_argument('filepath', type=str, help='file containing the game')
    parser.add_argument('print_output', type=str, nargs='?', default="None",
                        choices=['Verbose', 'Brief', 'None'],
                        help='controls what the algorithm will print for output')
    parser.add_argument('simulations', type=int, help='the number of simulations to run')


if __name__ == '__main__':
    # execute only if run as a script
    main()
"""




# Example usage:
if __name__ == "__main__":
    game = ConnectFour()
    game.play()