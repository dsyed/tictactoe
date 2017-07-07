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

    def get_current_player(self):
        """Return a string representation of the current player."""
        return Board.STATES[self.current_player]

    def switch_player(self):
        """Switch between X and O."""
        self.current_player ^= 1

    def move(self, y, x):
        """Move the current player's token onto the board and switch player."""
        self.state[y][x] = self.current_player
        self.switch_player()

    def __str__(self):
        """String representation of the board for display."""
        return '\n' + '\n'.join([' '.join([Board.STATES[el] for el in row]) for row in self.state])


board = Board()


def prompt(board):
    """A single turn of gameplay."""
    print board

    # Expected format: [y:number] [x:number]
    # These are the coordinates of the space
    space = raw_input('Where would you like to place {}: '.format(board.get_current_player()))
    y, x = [int(coord) for coord in space.split()]

    board.move(y, x)

while True:
    prompt(board)
