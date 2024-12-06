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


def search_around(wordsearch, row, column, value):
    matched_characters = []
    offsets = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    for offset in offsets:
        if row + offset[0] < 0 or column + offset[1] < 0:
            continue
        if row + offset[0] >= len(wordsearch) or column + offset[1] >= len(
            wordsearch[0]
        ):
            continue
        char = wordsearch[row + offset[0]][column + offset[1]]
        if char == value:
            matched_characters.append(
                {
                    "position": (row + offset[0], column + offset[1]),
                    "offset": offset,
                    "character": char,
                }
            )

    return matched_characters


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
            current_character = {
                "position": (x, y),
                "offset": [0, 0],
                "character": column,
            }
            if column == "A":
                matched_characters_m = search_around(wordsearch, x, y, "M")
                if len(matched_characters_m) != 2:
                    continue
                matched_characters_s = []
                for m_character in matched_characters_m:
                    offset = [x * -1 for x in m_character["offset"]]
                    test = search_direction(wordsearch, x, y, "S", offset)
                    if test:
                        matched_characters_s.append(test)
                if len(matched_characters_s) != 2:
                    continue
                matches.append(
                    {
                        "current_character": current_character,
                        "m_characters": matched_characters_m,
                        "s_characters": matched_characters_s,
                    }
                )
    print(len(matches))


if __name__ == "__main__":
    main()
