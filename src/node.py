import random
import copy
import connect_four


class Node:
    def __init__(self, state, move=None, parent=None, player=None):
        """
        Initialize a node in the game tree.

        Parameters:
        - current_game: the game state at the current node
        - move: The move that led to this node from its parent (None if this is the root).
        - parent: The parent node (None if this is the root).
        """
        self.state = state # the game state at this node; a ConnectFour object
        self.move = move  # The move leading to this node
        self.parent = parent  # Parent node
        self.children = []  # List of child nodes
        self.wins = 0  # Wins for this node
        self.visits = 0  # Number of times this node has been visited
        self.is_terminal = False  # Flag for terminal nodes (win/loss/draw)
        self.player = player  # player associated with this node
        self.terminal_value = 0

    def add_child(self, child_state, move, player):
        """Create a new child node representing a move and add it to this node's children."""
        child_node = Node(state=child_state, move=move, parent=self, player=player)
        child_node.update_terminal_status()  # Check and update the terminal status for the child node
        self.children.append(child_node)

    def update(self, result):
        """
        Update node statistics after a simulation.

        Parameters:
        - result: -1 for a Red win, 0 for a draw, 1 for a Yellow win.
        """
        self.visits += 1  # Always increment visits

        if result == -1:  # Red wins
            if self.player == 'R':  # If this node represents Red
                self.wins += 1
        elif result == 1:  # Yellow wins
            if self.player == 'Y':  # If this node represents Yellow
                self.wins += 1
        # If it's a draw (result == 0), do nothing with wins, just increment visits

    def select_random_child(self):
        """Selects a random child node"""
        return random.choice(self.children) if self.children else None

    def get_move_sequence(self):
        """Retrieve the sequence of moves from the root to this node."""
        sequence = []
        current_node = self
        while current_node.parent is not None:
            sequence.append(current_node.move)
            current_node = current_node.parent
        return sequence[::-1]  # Reverse to get sequence from root to this node

    def is_leaf(self):
        """Check if the node is a leaf, meaning it has no children."""
        return len(self.children) == 0

    def is_fully_expanded(self):
        """Check if all possible moves from this node have been expanded."""
        return len(self.children) > 0 and all(child.visits > 0 for child in self.children)

    def update_terminal_status(self):
        """Check the state and update the terminal status."""
        if self.state.game_over:  # checks if game is complete
            self.is_terminal = True

    def expand_node(self, print_out='None'):
        # Make a deep copy of the current game state
        game_copy = copy.deepcopy(self.state)  # Assuming self.state is an instance of ConnectFour
        game_copy.update_game_status()
        game_copy.update_valid_moves()
        possible_moves = game_copy.valid_moves  # Get all legal moves

        # Get the next player
        next_player = 'R' if game_copy.current_player == 'R' else 'Y'

        # Loop through each possible move
        for move in possible_moves:
            # Create a new child state by copying the current game state
            child_state = copy.deepcopy(game_copy)  # Deep copy to ensure independence
            child_state.make_move(move)  # Apply the move to the copied state
            # Create a child node for this move
            self.add_child(child_state, move, next_player)

            if (print_out=='Verbose'):
                print(f'NODE ADDED for {next_player} player for move {move}')

    def simulate_from_node(self, print_out='None'):
        """
        Perform a random simulation from the current node.

        Returns:
        - result: +1 for a win, 0 for a draw, -1 for a loss.
        """
        # Create a deep copy of the current state for simulation
        current_state = copy.deepcopy(self.state)

        # some helper print statements
        # print(f'simulation for \'{self.player}\' into col {self.move}')
        # print(current_state.display_board())

        while not current_state.game_over:  # Continue until the game is over
            legal_moves = current_state.valid_moves  # Get all legal moves
            # print(f'legal moves for {current_state.current_player}: {legal_moves}', end=' ')
            move = random.choice(legal_moves)  # Select a random legal move

            if(print_out=='Verbose'):
                print(f'Move selected: {move}')

            current_state.make_move(move)  # Apply the selected move

        # Return the result of the game from the perspective of the current player
        if current_state.winner == 'R':
            #if (print_out=='Verbose'):
             #   print(f'Simulated winner: -1')
            return -1  # Player 'R' wins
        elif current_state.winner == 'Y':
           #if (print_out=='Verbose'):
             ##   print(f'Simulated winner: 1')
            return 1  # Player 'Y' wins
        elif current_state.draw:
            #if (print_out=='Verbose'):
            #    print(f'Simulated winner: 0')
            return 0  # Draw
        else:
            return 2  # Unexpected result; should not reach here



    def __repr__(self):
        return f"Node(move={self.move}, wins={self.wins}, visits={self.visits})"
