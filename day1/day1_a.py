from utils import read_infile

depths = [int(s) for s in read_infile('input_day1.txt')]
depth_pairs = zip(depths[:-1], depths[1:])
num_increase = sum(pair[1] > pair[0] for pair in depth_pairs)
print(f'Number of increases: {num_increase}')   # 1832
