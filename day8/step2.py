import numpy as np


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def main():
    lines = read_input("day8/input.txt")
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
                direction = partner_tower - tower
                test_case = tower + direction
                while (
                    test_case[0] >= 0
                    and test_case[0] < len(grid)
                    and test_case[1] >= 0
                    and test_case[1] < len(grid[0])
                ):
                    results.append(
                        (test_case[0], test_case[1])
                    )  ## just appending test case appends a reference
                    test_case += direction
                test_case = tower - direction
                while (
                    test_case[0] >= 0
                    and test_case[0] < len(grid)
                    and test_case[1] >= 0
                    and test_case[1] < len(grid[0])
                ):
                    results.append((test_case[0], test_case[1]))
                    test_case -= direction
    print(len(np.unique(results, axis=0)))


if __name__ == "__main__":
    main()
