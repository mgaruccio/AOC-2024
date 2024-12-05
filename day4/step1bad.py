import numpy as np

SEARCH_TERM = "XMAS"


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def search_for_term(search_list, term):
    matches = 0
    for i in range(len(search_list)):
        if "".join(search_list[i : i + len(term)]) == term:
            matches += 1
    return matches


def search_for_term_in_diagonals(wordsearch, term):
    search_list = np.diag(wordsearch)
    matches = search_for_term(search_list, term)
    max_offset = len(wordsearch)
    for offset in range(1, max_offset):
        search_list = np.diag(wordsearch, offset)
        matches += search_for_term(search_list, term)
        search_list = np.diag(wordsearch, -offset)
        matches += search_for_term(search_list, term)
    return matches


def search_for_term_in_rows(wordsearch, term):
    matches = 0
    for row in wordsearch:
        matches += search_for_term(row, term)
    return matches


def search_for_term_in_columns(wordsearch, term):
    matches = 0
    for col in wordsearch.T:
        matches += search_for_term(col, term)
    return matches


def main():
    lines = read_input("day4/input.txt")
    lines = [list(line) for line in lines]
    wordsearch = np.array(lines)
    matches = 0

    # Original orientation
    matches += search_for_term_in_rows(wordsearch, SEARCH_TERM)
    matches += search_for_term_in_columns(wordsearch, SEARCH_TERM)
    matches += search_for_term_in_diagonals(wordsearch, SEARCH_TERM)

    # Left-right flip
    flipped_lr = np.fliplr(wordsearch)
    matches += search_for_term_in_rows(flipped_lr, SEARCH_TERM)
    matches += search_for_term_in_columns(flipped_lr, SEARCH_TERM)
    matches += search_for_term_in_diagonals(flipped_lr, SEARCH_TERM)

    # Up-down flip
    flipped_ud = np.flipud(wordsearch)
    matches += search_for_term_in_rows(flipped_ud, SEARCH_TERM)
    matches += search_for_term_in_columns(flipped_ud, SEARCH_TERM)
    # matches += search_for_term_in_diagonals(flipped_ud, SEARCH_TERM)

    # flip both
    flipped_both = np.flipud(np.fliplr(wordsearch))

    matches += search_for_term_in_diagonals(flipped_both, SEARCH_TERM)

    print(f"Total matches: {matches}")


if __name__ == "__main__":
    main()
