import itertools
import functools
import operator
from multiprocessing import Pool, freeze_support


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def concat(x, y):
    return int(f"{x}{y}")


def calculate_next(current_value, next_value, ops):
    # return [op(current_value, next_value) for op in ops]
    vals = []
    for op in ops:
        new_val = op(current_value, next_value)
        vals.append(new_val)
    return vals


def get_potential_values(inputs):
    values = [inputs.pop(0)]
    while len(inputs) > 0:
        i = inputs.pop(0)
        new_vals = []
        for value in values:
            new_values = calculate_next(value, i, OPERATORS)
            new_vals.extend(new_values)
        values = new_vals
    return values


OPERATORS = [operator.add, operator.mul, concat]


def main():
    lines = read_input("day7/input.txt")
    cases = []
    final_results = []
    for line in lines:
        split_line = line.split(":")
        cases.append(
            {
                "test_case": int(split_line[0]),
                "inputs": [int(x) for x in split_line[1].lstrip().split(" ")],
            }
        )

    for case in cases:
        values = get_potential_values(case["inputs"])
        if case["test_case"] in values:
            final_results.append(case["test_case"])

    print(final_results)
    print(sum(final_results))


if __name__ == "__main__":
    main()
