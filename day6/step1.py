from pprint import pprint


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


START = "^"
OBSTACLE = "#"
DIRECTIONS = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]  # up, right, down, left


def find_start(grid):
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            if column == START:
                return (row_index, column_index)


def in_bounds(grid, position):
    return (
        position[0] >= 0
        and position[0] < len(grid)
        and position[1] >= 0
        and position[1] < len(grid[0])
    )


def check_obstacle(grid, position):
    return grid[position[0]][position[1]] == OBSTACLE


def next_position(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def fill_grid(grid, visited):
    """meant to fill the grid with the visited positions for debugging"""
    for position in visited:
        grid[position[0]][position[1]] = "X"
    grid_joined_rows = ["".join(row) for row in grid]
    return grid_joined_rows


def main():
    lines = read_input("day6/test_input.txt")
    grid = [list(line) for line in lines]
    ## grid is a 2d array of characters.  first position is the row, second is the column
    position = find_start(grid)
    direction = 0
    visited = [position]
    steps = 0
    while in_bounds(grid, position):
        steps += 1
        candidate_position = next_position(position, DIRECTIONS[direction])
        if not in_bounds(grid, candidate_position):
            break
        if check_obstacle(grid, candidate_position):
            direction = (direction + 1) % len(
                DIRECTIONS
            )  # turn right, wrapping around when we get to the end
            continue
        else:
            position = candidate_position
            visited.append(position)
    print(len(set(visited)))
    print(steps)
    # filled_grid = fill_grid(grid, visited)
    # pprint(filled_grid)


if __name__ == "__main__":
    main()
