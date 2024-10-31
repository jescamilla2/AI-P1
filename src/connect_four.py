
class ConnectFour:
    def __init__(self):
        # Initialize a 6x7 board with 'O' representing empty slots
        self.board = [['O'] * 7 for _ in range(6)]
        # Dictionary to map player symbols to their respective colors
        self.players = {'R': 'Red', 'Y': 'Yellow'}
        # Track the current player
        self.current_player = 'R'
        # keep track of valid moves left
        self.valid_moves = [col for col in range(7)]
        # Track the game status
        self.game_over = False
        # Status of game
        self.winner = None
        # if it's a draw
        self.draw = False

    def load_board(self, board_array, player):
        """Loads a specified 2D array into the board."""
        self.current_player = player

        if len(board_array) == 6 and all(len(row) == 7 for row in board_array):
            self.board = board_array
        else:
            raise ValueError("Invalid board size. Expected a 6x7 board.")

        self.update_valid_moves()
        self.update_game_status()

    def display_board(self):
        """Prints the current state of the board."""
        for row in self.board:
            print(' '.join(row))  # Join each row's elements with spaces for better readability
        print("0 1 2 3 4 5 6")  # Column numbers for user reference

    def is_valid_move(self, col):
        """Checks if the column is valid for a move."""
        return self.board[0][col] == 'O'  # Valid if the top row of the column is empty

    def update_valid_moves(self):
        """Updates the list of valid moves based on the current board state."""
        self.valid_moves = [col for col in range(7) if self.is_valid_move(col)]

    def update_game_status(self):
        # Check for a winner or a draw and update game status
        if self.check_winner(self.current_player):
            self.game_over = True
            self.winner = self.current_player
            return {'game_over': True, 'winner': self.winner, 'message': 'Player wins!'}
        elif self.is_draw():
            self.game_over = True
            self.draw = True
            return {'game_over': True, 'winner': None, 'message': 'It\'s a draw!'}
        else:
            self.update_valid_moves()  # Update valid moves after making the move
            self.switch_player()  # Switch to the next player
            return {'game_over': False, 'winner': None, 'message': 'Game continues'}

    def make_move(self, col):
        """Places the current player's piece in the specified column and updates the board."""
        if self.is_valid_move(col):
            for row in reversed(self.board):  # Start from the bottom row to find the lowest available slot
                if row[col] == 'O':  # If the slot is empty
                    row[col] = self.current_player  # Place the player's piece
                    break

            self.update_game_status()

        return False

    def check_winner(self, piece):
        """Checks for a win condition for the specified piece."""
        # Check horizontal, vertical, and diagonal for four-in-a-row
        return (self._check_horizontal(piece) or
                self._check_vertical(piece) or
                self._check_diagonal(piece))

    def _check_horizontal(self, piece):
        """Checks horizontal win condition."""
        for row in self.board:
            count = 0  # Initialize count of consecutive pieces
            for cell in row:
                if cell == piece:
                    count += 1  # Increment count if piece matches
                    if count == 4:  # Check if there are four in a row
                        return True
                else:
                    count = 0  # Reset count if not matching
        return False

    def _check_vertical(self, piece):
        """Checks vertical win condition."""
        num_rows = len(self.board)  # Get the number of rows
        num_cols = len(self.board[0])  # Get the number of columns

        for col in range(num_cols):  # Iterate over each column
            count = 0  # Initialize count of consecutive pieces
            for row in range(num_rows):  # Iterate over each row
                if self.board[row][col] == piece:
                    count += 1  # Increment count if piece matches
                    if count == 4:  # Check if there are four in a column
                        return True
                else:
                    count = 0  # Reset count if not matching
        return False

    def _check_diagonal(self, piece):
        """Checks diagonal win conditions."""
        num_rows = len(self.board)  # Get the number of rows
        num_cols = len(self.board[0])  # Get the number of columns

        # Check for diagonals from bottom-left to top-right
        for row in range(3, num_rows):  # Start from row 3 to allow room for diagonal
            for col in range(num_cols - 3):  # Check up to column num_cols - 4 for diagonal
                if (self.board[row][col] == piece and
                        self.board[row - 1][col + 1] == piece and
                        self.board[row - 2][col + 2] == piece and
                        self.board[row - 3][col + 3] == piece):
                    return True

        # Check for diagonals from bottom-right to top-left
        for row in range(3, num_rows):  # Start from row 3 to allow room for diagonal
            for col in range(3, num_cols):  # Check from column 3 to num_cols - 1 for diagonal
                if (self.board[row][col] == piece and
                        self.board[row - 1][col - 1] == piece and
                        self.board[row - 2][col - 2] == piece and
                        self.board[row - 3][col - 3] == piece):
                    return True

        return False

    def switch_player(self):
        """Switches the current player."""
        self.current_player = 'Y' if self.current_player == 'R' else 'R'

    def is_draw(self):
        # If no empty slots remain and no winner, it's a draw
        return all(cell != 'O' for row in self.board for cell in row)








