from pprint import pprint
from graphlib import TopologicalSorter

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


## generates a set of depdencies for each character
## this means that each key must come after all of the values
def order_rules(rules):
    second_chars = list(set([rule[1] for rule in rules]))
    precedence_rules = {}
    for char in second_chars:
        precedence_rule = [rule for rule in rules if rule[1] == char]
        precedence_rules[precedence_rule[0][1]] = [r[0] for r in precedence_rule]
    return precedence_rules


def order_update(update, rules):
    """Order update based on rules"""
    graph = {}
    for value in update:
        if value not in rules:
            continue
        graph[value] = rules[value]

    ts = TopologicalSorter(graph)
    sorted_update = tuple(ts.static_order())
    return [i for i in sorted_update if i in update]


def main():
    lines = read_input("day5/input.txt")
    rules = lines[:SECTION_BREAK]
    rules = [rule.split("|") for rule in rules]
    rules = [(int(rule[0]), int(rule[1])) for rule in rules]
    updates = lines[SECTION_BREAK + 1 :]
    updates = [update.split(",") for update in updates]
    updates = [[int(update) for update in update] for update in updates]
    ordered_rules = order_rules(rules)
    print(ordered_rules)
    invalid_updates = []
    middle_char_total = 0
    for update in updates:
        if not validate_update(update, rules):
            update = order_update(update, ordered_rules)
            invalid_updates.append(update)
            middle_char = update[len(update) // 2]
            middle_char_total += middle_char

    pprint(invalid_updates)
    print(middle_char_total)


if __name__ == "__main__":
    main()
