# tree.py
import copy
import connect_four

from node import Node
import random
import math


class Tree:
    def __init__(self, root_state):
        """
        Initialize the game tree with a root node.

        Parameters:
        - root_state: The initial state of the game at the root of the tree.
        """
        # Get the player who just moved
        prior_player = 'Y' if root_state.current_player == 'R' else 'R'

        self.root = Node(root_state, player=prior_player)  # Root node of the tree
        self.current_node = self.root # keeps track of tree traversal

    def select(self, algorithm_type='PMCGS', print_out='None'):
        """Select a node to expand based on the given algorithm."""
        current_node = self.root

        while not current_node.is_terminal:
            if not current_node.is_fully_expanded():
                break
            if algorithm_type == 'UCT':
                current_node = self._ucb_select(current_node)

                if (print_out=='Verbose'):
                    print(f'wi: {current_node.wins}; ni: {current_node.visits}; Move selected: {current_node.move}')

            else:  # Default to PMCGS
                current_node = random.choice(current_node.children)
                # print statements
                if (print_out=='Verbose'):
                    print(f'wi: {current_node.wins}; ni: {current_node.visits}; Move selected: {current_node.move}')

        if (current_node.is_terminal):
            # update terminal node value for printing purposes
            if (current_node.player == 'R'):
                current_node.terminal_value = -1
            elif (current_node.player == 'Y'):
                current_node.terminal_value = 1
            if (print_out == 'Verbose'):
                print(f'TERMINAL NODE VALUE: {current_node.terminal_value}')

        return current_node

    def backpropagate(self, node, result, print_out='None'):
        """Backpropagate the simulation result up the tree."""
        while node:
            node.update(result)

            if (print_out=='Verbose'):
                print(f'Updated values - wi: {node.wins}; ni: {node.visits}')

            node = node.parent

    def _ucb_select(self, node, c=1.4):
        """Select a child of this node using the UCB1 formula."""
        best_child = max(
            node.children,
            key=lambda child: (child.wins / child.visits) +
                              c * math.sqrt(math.log(node.visits) / child.visits)
        )
        return best_child

    def best_move_uct(self):
        """Return the child with the highest win rate (best explored move)."""
        # Guard against division by zero for win rate calculation
        best_child = max(
            (child for child in self.root.children if child.visits > 0),
            key=lambda child: child.wins / child.visits
        )
        return best_child.move

    def reset_root(self, new_root):
        """Reset the root of the tree to a new root node."""
        self.root = new_root
