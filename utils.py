def read_infile(filename: str) -> list[str]:
    """Read input file, strip newline chars, return list of lines."""
    with open(filename) as infile:
        in_lines = [line.strip() for line in infile.readlines()]
    return in_lines

