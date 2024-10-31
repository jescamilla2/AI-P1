import random
import math
import connect_four as c4
from node import Node
from tree import Tree


def uniform_random_move(game, print_out=False):
    """Baseline algorithm that randomly selects from available moves."""
    num_cols = len(game.board[0])  # Get the number of columns from the board
    legal_moves = [col for col in range(num_cols) if game.is_valid_move(col)]

    move = random.choice(legal_moves) if legal_moves else None

    if (print_out):
        print(f'FINAL Move selected: {move}')

    return move


def pmcgs_move(game, num_simulations, print_out='None'):
    """
    Pure Monte Carlo Game Search (PMCGS) function to select the best move in a Connect Four game.

    Parameters:
    - game: ConnectFour object representing the current state of the game.
    - num_simulations: Total number of simulations to perform.

    Returns:
    - The best move determined by the PMCGS process.
    """
    # Step 1: Initialize the Tree with the root state
    tree = Tree(game)
    if (print_out=='Verbose' or print_out=='Brief'):
        print(f'root player is: {tree.root.player}')

    for _ in range(num_simulations):
        # Step 2: Selection phase - Select a node to expand
        selected_node = tree.select(algorithm_type='PMCGS', print_out=print_out)

        # If we reach a terminal node, backpropagate the result and continue
        if selected_node.is_terminal:
            result = selected_node.simulate_from_node(print_out=print_out)  # Simulate directly from terminal state
            tree.backpropagate(selected_node, result, print_out=print_out)
            continue

        # Step 3: Expansion phase - Expand all legal moves from the selected node
        selected_node.expand_node(print_out=print_out)  # Expands all possible child nodes for the selected node

        # Step 4: Simulation phase - Simulate for each child node and backpropagate results
        for child in selected_node.children:
            result = child.simulate_from_node(print_out=print_out)  # Simulate a random playthrough from this child node
            tree.backpropagate(child, result, print_out=print_out)  # Backpropagate the result from this child

    # print the win rates of different moves
    for child in tree.root.children:
        # Calculate win rate; guard against division by zero
        win_rate = child.wins / child.visits if child.visits > 0 else 0.0
        if (print_out=='Verbose'):
            print(f'Column {child.move}: {win_rate:.2f}')


    # After all simulations, return the move of the most visited child of the root
    best_node = tree.root.select_random_child()

    if best_node is None:
        print('No viable children')
    else:
        if (print_out=='Verbose' or print_out=='Brief'):
            print(f'FINAL Move selected: {best_node.move}')
        return best_node.move


def uct_move(game, num_simulations, print_out='None'):
    """
    UCT function to select the best move in a Connect Four game.

    Parameters:
    - game: ConnectFour object representing the current state of the game.
    - num_simulations: Total number of simulations to perform.

    Returns:
    - The best move determined by the PMCGS process.
    """
    # Step 1: Initialize the Tree with the root state
    tree = Tree(game)
    if (print_out == 'Verbose' or print_out == 'Brief'):
        print(f'root player is: {tree.root.player}')

    for _ in range(num_simulations):
        # Step 2: Selection phase - Select a node to expand
        selected_node = tree.select(algorithm_type='UCT', print_out=print_out)

        # If we reach a terminal node, backpropagate the result and continue
        if selected_node.is_terminal:
            result = selected_node.simulate_from_node(print_out=print_out)  # Simulate directly from terminal state
            tree.backpropagate(selected_node, result, print_out=print_out)
            continue

        # Step 3: Expansion phase - Expand all legal moves from the selected node
        selected_node.expand_node(print_out=print_out)  # Expands all possible child nodes for the selected node

        # Step 4: Simulation phase - Simulate for each child node and backpropagate results
        for child in selected_node.children:
            result = child.simulate_from_node(print_out=print_out)  # Simulate a random playthrough from this child node
            tree.backpropagate(child, result, print_out=print_out)  # Backpropagate the result from this child

    # print the win rates of different moves
    for child in tree.root.children:
        # Calculate win rate; guard against division by zero
        win_rate = child.wins / child.visits if child.visits > 0 else 0.0
        if (print_out == 'Verbose'):
            print(f'Column {child.move}: {win_rate:.2f}')


    # After all simulations, return the move of the most visited child of the root
    best_move = tree.best_move_uct()

    if (print_out == 'Verbose' or print_out == 'Brief'):
        print(f'FINAL Move selected: {best_move}')
    return best_move


'''
def uct_move(game, simulations=500, exploration=1.41):
    """uses the upper confidence bound to decide moves by balancing exploration and exploitation"""
    stats = {col: {'wins': 0, 'simulations': 0} for col in range(7) if game.is_valid_move(col)}

    for _ in range(simulations):
        for col in stats:
            # Clone game state
            sim_game = deepcopy(game)
            sim_game.make_move(col)

            # Simulate randomly to the end of the game
            while not sim_game.check_winner() and not sim_game.is_draw():
                random_col = uniform_random_move(sim_game)
                sim_game.make_move(random_col)
                sim_game.switch_player()

            # Update win/loss for current player
            if sim_game.check_winner() and sim_game.current_player == game.current_player:
                stats[col]['wins'] += 1
            stats[col]['simulations'] += 1

    # Calculate UCB values and select the move with the highest UCB
    def ucb(win, sim, total_sim):
        return (win / sim) + exploration * math.sqrt(math.log(total_sim) / sim)

    total_simulations = sum(s['simulations'] for s in stats.values())
    best_move = max(stats, key=lambda col: ucb(stats[col]['wins'], stats[col]['simulations'], total_simulations))
    return best_move
'''
