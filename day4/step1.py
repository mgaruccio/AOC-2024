# import numpy as np
from pprint import pprint


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def remove_negative_positions(offsets, row, column):
    return [
        offset for offset in offsets if row + offset[0] >= 0 and column + offset[1] >= 0
    ]


def remove_out_of_bounds_positions(positions, wordsearch, row, column):
    return [
        pos
        for pos in positions
        if pos[0] + row < len(wordsearch) and pos[1] + column < len(wordsearch[0])
    ]


def search_around_(wordsearch, row, column, value):
    candidates = []
    positions_to_check = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
        [1, 1],
        [-1, -1],
        [1, -1],
        [-1, 1],
    ]

    positions_to_check = remove_negative_positions(positions_to_check, row, column)
    positions_to_check = remove_out_of_bounds_positions(
        positions_to_check, wordsearch, row, column
    )

    for pos in positions_to_check:
        if wordsearch[row + pos[0]][column + pos[1]] == value:
            candidates.append([(row + pos[0], column + pos[1]), pos])

    return candidates


def search_direction(wordsearch, row, column, value, direction):
    position_to_check = (row + direction[0], column + direction[1])

    if position_to_check[0] < len(wordsearch) and position_to_check[1] < len(
        wordsearch[0]
    ):
        if wordsearch[position_to_check[0]][position_to_check[1]] == value:
            return (position_to_check, direction)


def main():
    lines = read_input("day4/input.txt")
    wordsearch = [list(line) for line in lines]
    matches = []

    for x, row in enumerate(wordsearch):
        for y, column in enumerate(row):
            if column == "X":
                candidates = search_around_(wordsearch, x, y, "M")
                new_candidates = []
                for candidate in candidates:
                    new_candidates.append(
                        search_direction(
                            wordsearch,
                            candidate[0][0],
                            candidate[0][1],
                            "A",
                            candidate[1],
                        )
                    )
                    new_candidates = [x for x in new_candidates if x]
                for candidate in new_candidates:
                    if search_direction(
                        wordsearch, candidate[0][0], candidate[0][1], "S", candidate[1]
                    ):
                        matches.append(
                            search_direction(
                                wordsearch,
                                candidate[0][0],
                                candidate[0][1],
                                "S",
                                candidate[1],
                            )
                        )

    matches = [x for x in matches if x[0][0] >= 0 and x[0][1] >= 0]
    print(len(matches))
    # pprint(matches)


if __name__ == "__main__":
    main()
