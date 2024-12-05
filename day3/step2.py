import re


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def find_mul_calls(txt):
    return re.findall("mul\(\d+,\d+\)", txt)


def extract_numbers(txt):
    numbers = re.findall("\d+", txt)
    return [int(n) for n in numbers]


def scrub_line(txt):
    return re.sub("don't\(\)(.*?)do\(\)", "", txt)


if __name__ == "__main__":
    lines = read_input("day3/input.txt")
    total = 0
    line = "".join(lines)

    print(line)
    line = scrub_line(line)

    mul_calls = find_mul_calls(line)
    for call in mul_calls:
        numbers = extract_numbers(call)
        total += numbers[0] * numbers[1]
    print(total)