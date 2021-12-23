import sys

import numpy as np
from utils import read_infile
from dataclasses import dataclass
from typing import Iterable, Optional


class BingoBoard:
    def __init__(self, board_list: list[list[int]]) -> None:
        """Initialize board values and set all locations as unmarked"""
        self.last_called: int = None
        self.values: np.array = np.array(board_list, dtype=int)
        self.marked: np.array = np.array([False]*len(self.values.flat)).reshape(self.values.shape)

    def mark(self, value: int) -> None:
        """Mark the board locations where value is found"""
        self.last_called = value
        self.marked[self.values == value] = True

    def check_for_win(self) -> Optional[int]:
        """Checks a board for win condition. If win, returns the score. Else returns None."""
        if any((self.check_rows(), self.check_cols())):
            return self.score()
        else:
            return None

    def check_rows(self) -> bool:
        """Return True if any row is fully marked"""
        return any(all(row) for row in self.marked)

    def check_cols(self) -> bool:
        """Return True if any column is fully marked"""
        return any(all(col) for col in self.marked.transpose())

    # Woops diagonals don't count. Keeping this just in case part B wants it.
    # def check_diag(self) -> bool:
    #     """Return True if diagonal is fully marked"""
    #     return all(self.marked.diagonal())

    def score(self) -> int:
        """Return the sum of the unmarked values * the last called value"""
        return np.sum(self.values[~self.marked]) * self.last_called


def parse_infile(infile: str) -> dict:
    infile_lines = read_infile(infile)
    return_dict = {'boards': list()}
    
    # First line of the input is the bingo calls
    return_dict['calls'] = [int(s) for s in infile_lines[0].split(',')]

    # Subsequent lines are a blank line followed by the board grid
    # Start at the beginning of the first board
    board_rows = list()
    for line in infile_lines[2:]:
        if line != '':
            board_row = [int(s) for s in line.split()]
            board_rows.append(board_row)
        else:    # End of board rows, construct the board
            return_dict['boards'].append(BingoBoard(board_rows))
            # Re-init board_rows to start constructing the next board
            board_rows = list()

    # Looks like the input doesn't end with blank line, so need to add
    # the board after end of file
    return_dict['boards'].append(BingoBoard(board_rows))
    return return_dict


# infile = 'example_day4a.txt'
infile = 'input_day4a.txt'
infile_dict = parse_infile(infile)
calls: list[int] = infile_dict['calls']
boards: list[BingoBoard] = infile_dict['boards']

# Iterate through the calls until a winner is found, then return the score of the winner.
for call in calls:
    # print(call)
    for board in boards:
        board.mark(call)
        # print(board.values)
        # print(board.marked)
        # Walrus time
        if score := board.check_for_win():
            # Example: 4512. Puzzle: 11774
            print(f'Winner found. {score=}')
            print(f'Winning board values:\n{board.values}')
            print(f'Winning board marking:\n{board.marked}')
            sys.exit()
