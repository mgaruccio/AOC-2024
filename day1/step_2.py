def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def main():
    lines = read_input("day1/step_1_input.txt")
    lines = [line.split("   ") for line in lines]
    left_list = [int(line[0]) for line in lines]
    right_list = [int(line[1]) for line in lines]

    total = 0
    for item in left_list:
        instances = right_list.count(item)
        score = item * instances
        total += score

    print(total)


if __name__ == "__main__":
    main()
