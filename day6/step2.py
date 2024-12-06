from pprint import pprint
import copy
import threading
import concurrent.futures


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


START = "^"
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


def check_obstacle(grid, position, new_obstacle=None):
    if grid[position[0]][position[1]] or new_obstacle == position:
        return True
    return False


def next_position(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def fill_grid(grid, visited):
    """meant to fill the grid with the visited positions for debugging"""
    for position in visited:
        grid[position[0]][position[1]] = "X"
    grid_joined_rows = ["".join(row) for row in grid]
    return grid_joined_rows


def check_loop(grid, start_position, new_obstacle=None):
    position = start_position
    direction = 0
    steps = set()
    while in_bounds(grid, position):
        candidate_position = next_position(position, DIRECTIONS[direction])
        if (position, candidate_position) in steps:
            return "LOOP!"
        if not in_bounds(grid, candidate_position):
            steps.add(
                (position, candidate_position)
            )  # records both the prior and new position to allow for loop detection
            break
        if check_obstacle(grid, candidate_position, new_obstacle):
            direction = (direction + 1) % len(DIRECTIONS)
            continue
        else:
            steps.add(
                (position, candidate_position)
            )  # records both the prior and new position to allow for loop detection
            position = candidate_position

    return steps


def main():
    lines = read_input("day6/input.txt")
    grid = [list(line) for line in lines]
    ## grid is a 2d array of characters.  first position is the row, second is the column
    position = find_start(grid)
    ## this helps with performance by converting the grid to a boolean grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = True if grid[i][j] == "#" else False
    steps = check_loop(grid, position)
    positions = set([step[0] for step in steps])
    print(len(positions))

    potential_new_obstacles = positions

    obstacle_counter = 0
    loop_counter = 0
    for new_obstacle in potential_new_obstacles:
        loop_counter += 1
        steps = check_loop(grid, position, new_obstacle)
        if steps == "LOOP!":
            print(new_obstacle)
            print(loop_counter)
            obstacle_counter += 1

    print(obstacle_counter)

    # print(results)


if __name__ == "__main__":
    main()
