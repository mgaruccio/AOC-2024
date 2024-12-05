def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def analyze_report(report):
    """Analyze report and return 1 if the report is safe, otherwise 0"""
    if report[0] - report[1] > 0:
        start_direction = "decreasing"
    elif report[0] - report[1] < 0:
        start_direction = "increasing"
    else:
        return 0

    last_reading = report.pop(0)
    for reading in report:
        if reading == last_reading:
            return 0
        if last_reading - reading > 0:
            direction = "decreasing"
        else:
            direction = "increasing"
        if start_direction != direction:
            return 0

        diff = abs(last_reading - reading)
        if diff > 3:
            return 0
        last_reading = reading
    return 1


def main():
    lines = read_input("day2/input.txt")
    reports = [line.split(" ") for line in lines]
    reports = [[int(reading) for reading in report] for report in reports]

    safe_count = 0
    for report in reports:
        safe_count += analyze_report(report)

    print(safe_count)


if __name__ == "__main__":
    main()
