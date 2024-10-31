import random
import math
from algorithms import uniform_random_move
from algorithms import pmcgs_move
from algorithms import uct_move
from connect_four import ConnectFour
from node import Node
from tree import Tree


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



class Game:
    """models a game between two agents"""

    def __init__(self, agent1_algorithm, agent1_sims, agent2_algorithm, agent2_sims, num_games):
        self.agent1_algorithm = agent1_algorithm
        self.agent2_algorithm = agent2_algorithm
        self.agent1_sims = agent1_sims
        self.agent2_sims = agent2_sims
        self.num_games = num_games
        self.agent1_wins = 0
        self.agent2_wins = 0
        self.draws = 0

    def play(self):
        """plays a single game between two agents"""
        game = ConnectFour()  # Start a new game instance

        while not game.game_over:
            if game.current_player == 'R':
                move = best_move(game, algorithm=self.agent1_algorithm, simulations=self.agent1_sims, print_out='None')
            else:
                move = best_move(game, algorithm=self.agent2_algorithm, simulations=self.agent2_sims, print_out='None')

            if move is not None:
                game.make_move(move)  # Apply the selected move

            else:
                break

        # Record the result of the game
        if game.winner == 'R':
            self.agent1_wins += 1
        elif game.winner == 'Y':
            self.agent2_wins += 1
        else:
            self.draws += 1


class Tournament:
    def __init__(self, agents, num_games):
        """takes in a dictionary of the different algorithms, roster is a tuple of (algorithm, sims)"""

        self.roster = agents
        self.matches = num_games
        self.results = {}


    def run(self):
        """runs the tournament"""

        # roster = [('UR', 0), ('PMCGS', 500), ('PMCGS', 10000), ('UCT', 500), ('UCT', 10000)]

        for i in range(len(self.roster) - 1):
            for j in range(i+1, len(self.roster)):
                agent1_algorithm = self.roster[i][0]
                agent2_algorithm = self.roster[j][0]

                agent1_sims = self.roster[i][1]
                agent2_sims = self.roster[j][1]

                match = Game(agent1_algorithm, agent1_sims, agent2_algorithm, agent2_sims, self.matches)
                for _ in range(match.num_games):
                    match.play()

                win_percentage = match.agent1_wins / match.num_games

                self.results[(i+1, j+1)] = win_percentage


    def display_results(self):
        """display the results"""
        print(f'The agents are:')
        for i in range(len(self.roster)):
            print(f'Agent {i+1}: {self.roster[i]}')

        print(f'The results of the tournament are:')

        for key, value in self.results.items():
            print(f'Matchup: {key}; Win-Percentage: {value:.2f}')



if __name__ == '__main__':

    agents = [('UR', 0), ('PMCGS', 10), ('PMCGS', 100), ('UCT', 10), ('UCT', 100)]

    tournament = Tournament(agents, 20)
    tournament.run()
    tournament.display_results()


