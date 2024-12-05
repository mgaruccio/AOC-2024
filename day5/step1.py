# SECTION_BREAK = 21
SECTION_BREAK = 1176


def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def validate_update(update, rules):
    """Validate update against rules"""
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        first_char = update.index(rule[0])
        try:
            update.index(rule[1], first_char + 1)
        except ValueError:
            return False

    return True


def main():
    lines = read_input("day5/input.txt")
    rules = lines[:SECTION_BREAK]
    rules = [rule.split("|") for rule in rules]
    updates = lines[SECTION_BREAK + 1 :]
    updates = [update.split(",") for update in updates]
    valid_updates = []
    middle_char_total = 0
    for update in updates:
        if validate_update(update, rules):
            valid_updates.append(update)
            middle_char = update[len(update) // 2]
            middle_char_total += int(middle_char)

    print(middle_char_total)


if __name__ == "__main__":
    main()
