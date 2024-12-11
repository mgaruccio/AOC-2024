import numpy as np


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def main():
    lines = read_input("day8/test_input.txt")
    lines = [list(line) for line in lines]
    grid = np.array(lines)
    print(grid)
    u = np.unique(grid)
    frequencies = np.delete(u, np.where(u == "."))
    frequencies = np.delete(frequencies, np.where(frequencies == "#"))
    results = []
    for f in frequencies:
        towers = (f, np.argwhere(grid == f))
        for tower in towers[1]:
            partner_towers = [t for t in towers[1] if not np.array_equal(t, tower)]
            for partner_tower in partner_towers:
                antinode = [
                    tower[0] - (partner_tower[0] - tower[0]),
                    tower[1] - (partner_tower[1] - tower[1]),
                ]
                if (
                    antinode[0] >= 0
                    and antinode[0] < len(grid)
                    and antinode[1] >= 0
                    and antinode[1] < len(grid[0])
                ):
                    results.append(antinode)
    print(len(np.unique(results, axis=0)))


if __name__ == "__main__":
    main()
