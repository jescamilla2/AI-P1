



class ConnectFour:
    def __init__(self):
        # Initialize a 6x7 board with 'O' representing empty slots
        self.board = [['O'] * 7 for _ in range(6)]
        # Dictionary to map player symbols to their respective colors
        self.players = {'R': 'Red', 'Y': 'Yellow'}
        # Track the current player
        self.current_player = 'R'
        # Track the game status
        self.game_over = False

    def display_board(self):
        """Prints the current state of the board."""
        for row in self.board:
            print(' '.join(row))  # Join each row's elements with spaces for better readability
        print("1 2 3 4 5 6 7")  # Column numbers for user reference

    def is_valid_move(self, col):
        """Checks if the column is valid for a move."""
        return self.board[0][col] == 'O'  # Valid if the top row of the column is empty

    def make_move(self, col, piece):
        """Places a piece in the specified column."""
        for row in reversed(self.board):  # Start from the bottom row to find the lowest available slot
            if row[col] == 'O':  # If the slot is empty
                row[col] = piece  # Place the player's piece
                break

    def check_winner(self, piece):
        """Checks for a win condition for the specified piece."""
        # Check horizontal, vertical, and diagonal for four-in-a-row
        return (self.check_horizontal(piece) or
                self.check_vertical(piece) or
                self.check_diagonal(piece))

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

    def play(self):
        """Main game loop for playing the game."""
        while not self.game_over:
            self.display_board()
            col = int(input(f"Player {self.players[self.current_player]}, choose a column (1-7): ")) - 1

            if col < 0 or col > 6:
                print("Invalid column! Please choose a column between 1 and 7.")
                continue

            if self.is_valid_move(col):
                self.make_move(col, self.current_player)  # Make the move for the current player
                if self.check_winner(self.current_player):  # Check if this move won the game
                    self.display_board()
                    print(f"Player {self.players[self.current_player]} wins!")
                    self.game_over = True  # End the game if there's a winner
                else:
                    self.switch_player()  # Switch to the next player
            else:
                print("Column is full! Please choose another column.")






