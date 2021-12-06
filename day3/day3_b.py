import numpy as np
from typing import Iterable
from functools import partial
from utils import read_infile


def common_in_column(numbers: np.ndarray, most_least: str, if_equal: int, column: int) -> int:
    num_ones = np.sum(numbers[:, column])
    num_zeros = numbers.shape[0] - num_ones
    if num_ones == num_zeros:
        return if_equal
    elif most_least == "most":
        return 1 if num_ones > num_zeros else 0
    elif most_least == "least":
        return 0 if num_ones > num_zeros else 1


def prune_numbers(numbers: np.ndarray, prune_func: callable, column: int = 0, debug: bool = False):
    if debug:
        print(f'Pruning column {column}')

    # Generate mask indicating which rows meet the condition
    keep_value = prune_func(numbers=numbers, column=column)
    if debug:
        print(f'Column {column} {keep_value=}')
    mask = numbers[:, column] == keep_value

    # Keep only the rows that meet the pruning condition
    pruned_array = numbers[mask]
    if debug:
        print(f'{pruned_array=}')
    if len(pruned_array) == 1:  # Finished when we reach one row
        return pruned_array[0]
    else:                       # Otherwise, repeat on the next column
        return prune_numbers(pruned_array, prune_func, column + 1, debug=debug)


def packbits(bit_list: Iterable[int]) -> int:
    return int(''.join(str(v) for v in bit_list), 2)


# # Example input
# example_input = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""
# input_strings = example_input.split("\n")

# Puzzle input
input_strings = read_infile('input_day3.txt')

input_ints = np.array([[int(v) for v in substr] for substr in input_strings])

# Generate the pruning function partials for the two ratings. O2 is most common element, 1 if equal.
# CO2 is least common element, 0 if equal.
o2_func = partial(common_in_column, most_least="most", if_equal=1)
co2_func = partial(common_in_column, most_least="least", if_equal=0)

oxygen_rating = packbits(prune_numbers(input_ints, prune_func=o2_func))
co2_rating = packbits(prune_numbers(input_ints, prune_func=co2_func))

# Example: oxygen_rating=23, co2_rating=10, product=230
# Puzzle: oxygen_rating=3939, co2_rating=1762, product=6940518
print(f'{oxygen_rating=}, {co2_rating=}, product={oxygen_rating * co2_rating}')
