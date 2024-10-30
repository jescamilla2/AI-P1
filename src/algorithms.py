import random
import math
import connect_four as c4



def uniform_random_move(game):
    """Baseline algorithm that randomly selects from available moves."""
    num_cols = len(game.board[0])  # Get the number of columns from the board
    legal_moves = [col for col in range(num_cols) if game.is_valid_move(col)]
    return random.choice(legal_moves) if legal_moves else None


def pmcgs(game, simulations=500):
    """simulates random plays for each legal move and selects the one with the highest win rate"""
    move_win_rate = {}

    for col in range(7):
        if not game.is_valid_move(col):
            continue

        wins = 0
        for _ in range(simulations):
            # Clone game state
            sim_game = deepcopy(game)
            sim_game.make_move(col)

            # Simulate until end
            while not sim_game.check_winner() and not sim_game.is_draw():
                random_col = uniform_random_move(sim_game)
                sim_game.make_move(random_col)
                sim_game.switch_player()

            if sim_game.check_winner() and sim_game.current_player == game.current_player:
                wins += 1  # Win for the starting player

        move_win_rate[col] = wins / simulations

    # Choose move with highest win rate
    return max(move_win_rate, key=move_win_rate.get)





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