from submarine_day2a import Submarine
from utils import read_infile


# Example input
# example = '''forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2'''
#
# move_strings = example.split("\n")

# Puzzle input
move_strings = read_infile("input_day2.txt")

movements = [(s.split()[0], int(s.split()[1])) for s in move_strings]
sub = Submarine()
for movement in movements:
    sub.move(*movement)
print(f'Horizontal position: {sub.position.x}; Vertical position: {sub.position.z}. '
      f'Product: {sub.position.x * sub.position.z}')    # Example: 150. Puzzle: 2102357.
