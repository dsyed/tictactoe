#!/usr/bin/env python

"""A simple tic-tac-toe game."""


class Board(object):
    """A tic-tac-toe board."""

    STATES = ['O', 'X', '_']

    def __init__(self):
        """Return a Board object."""
        self.current_player = 1
        self.state = [
            [2, 2, 2],
            [2, 2, 2],
            [2, 2, 2]
        ]
        self.win_counter = [
            {
                'row': [0, 0, 0],
                'col': [0, 0, 0],
                'dia': [0, 0]
            },
            {
                'row': [0, 0, 0],
                'col': [0, 0, 0],
                'dia': [0, 0]
            }
        ]

    def get_current_player(self):
        """Return a string representation of the current player."""
        return Board.STATES[self.current_player]

    def switch_player(self):
        """Switch between X and O."""
        self.current_player ^= 1

    def check_winner(self, dim, i):
        """Check if a player has won the game."""
        self.win_counter[self.current_player][dim][i] += 1

        if (self.win_counter[self.current_player][dim][i] == 3):
            print self
            print '{} wins!'.format(self.get_current_player())
            raise SystemExit

    def move(self, row, col):
        """Move the current player's token onto the board and switch player."""
        self.state[row][col] = self.current_player

        self.check_winner('row', row)
        self.check_winner('col', col)

        # NW-SE diagonal can be represented by `x = y`
        if (row == col):
            self.check_winner('dia', 0)
        
        # NE-SW diagonal can be represented by `x + y = 2`
        if (row + col == 2):
            self.check_winner('dia', 1)

        self.switch_player()

    def __str__(self):
        """String representation of the board for display."""
        return '\n' + '\n'.join([' '.join([Board.STATES[el] for el in row]) for row in self.state]) + '\n'


board = Board()


def prompt(board):
    """A single turn of gameplay."""
    print board

    # Expected format: [row:int] [col:int]
    # These are the coordinates of the space
    space = raw_input('Where would you like to place {}: '.format(board.get_current_player()))
    row, col = [int(coord) for coord in space.split()]

    board.move(row, col)

while True:
    prompt(board)
