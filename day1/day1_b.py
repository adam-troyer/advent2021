from utils import read_infile

# Example
# depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# Input file
depths = [int(s) for s in read_infile('input_day1.txt')]

depth_trios = zip(depths[:-2], depths[1:-1], depths[2:])
trio_sums = [sum(trio) for trio in depth_trios]
sum_pairs = zip(trio_sums[:-1], trio_sums[1:])
num_increase = sum(pair[1] > pair[0] for pair in sum_pairs)
print(f'Number of increases: {num_increase}')   # Example: 5. Real: 1858.
