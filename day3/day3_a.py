import numpy as np
from typing import Iterable
from utils import read_infile


def most_common_by_column(numbers: np.ndarray) -> np.ndarray:
    # 1 is most common if the sum of the column is > (# of rows / 2)
    target_sum = numbers.shape[0] / 2
    sum_by_col = np.sum(numbers, 0)
    most_common = np.fromiter((1 if v > target_sum else 0 for v in sum_by_col), dtype=int, count=numbers.shape[1])
    return most_common


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
gamma_bits = most_common_by_column(input_ints)
gamma = packbits(gamma_bits)
epsilon = packbits((0 if v == 1 else 1 for v in gamma_bits))

# Example: gamma=22, epsilon=9, consumption=198
# Puzzle: gamma=3135, epsilon=960, consumption=3009600
print(f'{gamma=}, {epsilon=}, power consumption={gamma*epsilon}')
