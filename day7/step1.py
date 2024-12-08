import itertools
import functools
import operator
from multiprocessing import Pool, freeze_support


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


OPERATORS = [operator.add, operator.mul]


def process_ops(args):
    ops, case = args
    i = None
    for x, op in enumerate(ops):
        values = case["inputs"]
        i = op((i if i else values[x]), values[x + 1])
    return i


def main():
    lines = read_input("day7/input.txt")
    cases = []
    for line in lines:
        split_line = line.split(":")
        cases.append(
            {
                "test_case": int(split_line[0]),
                "inputs": [int(x) for x in split_line[1].lstrip().split(" ")],
            }
        )

    final_results = 0
    case_count = len(cases)
    for x, case in enumerate(cases):
        print(f"Case {x + 1 } of {case_count}")
        ## Generates all possible comibations of operators
        opsets = itertools.combinations_with_replacement(
            OPERATORS, len(case["inputs"]) - 1
        )
        j = 0
        for opset in opsets:

            print(f"opset {j}")
            j += 1
            ## loops through all possible permutations of the operator set
            ## ends as soon as a valid result is found
            solved = False
            work_items = [(ops, case) for ops in set(itertools.permutations(opset))]
            ## not clear if this is working or not, I'm only seeing a single python process and it's only using one core
            with Pool(processes=10) as pool:
                results = pool.map(process_ops, work_items)
            for r in results:
                if r == case["test_case"]:
                    final_results += r
                    solved = True
                    break
            if solved:
                break

            # for ops in set(itertools.permutations(opset)):
            #     print(f"permutation {k}")
            #     i = process_ops(ops, case)
            #     if i == int(case["test_case"]):
            #         results.append(case["test_case"])
            #         break

    print(final_results)


if __name__ == "__main__":
    freeze_support()
    main()
