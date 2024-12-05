def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def main():
    lines = read_input("day1/step_1_input.txt")
    lines = [line.split("   ") for line in lines]
    left_list = [int(line[0]) for line in lines]
    right_list = [int(line[1]) for line in lines]
    left_list.sort()
    right_list.sort()

    total = 0

    for x, item in enumerate(left_list):
        distance = abs(right_list[x] - item)
        total += distance

    print(total)


if __name__ == "__main__":
    main()
