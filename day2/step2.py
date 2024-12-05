def read_input(filename):
    """Read input file and return list of strings, one per line"""
    with open(filename) as f:
        return f.read().splitlines()


def analyze_report(report):
    if report[0] - report[1] > 0:
        start_direction = "decreasing"
    elif report[0] - report[1] < 0:
        start_direction = "increasing"
    else:
        return False

    last_reading = report.pop(0)
    for reading in report:
        if reading == last_reading:
            return False
        if last_reading - reading > 0:
            direction = "decreasing"
        else:
            direction = "increasing"
        if start_direction != direction:
            return False

        diff = abs(last_reading - reading)
        if diff > 3:
            return False
        last_reading = reading
    return True


def main():
    lines = read_input("day2/input.txt")
    reports = [line.split(" ") for line in lines]
    reports = [[int(reading) for reading in report] for report in reports]

    safe_count = 0
    for report in reports:
        report_copy = report[:]
        if analyze_report(report_copy):
            safe_count += 1
            continue
        for pos in range(len(report)):
            report_copy = report[:]
            report_copy.pop(pos)
            if analyze_report(report_copy):
                safe_count += 1
                break

    print(safe_count)


if __name__ == "__main__":
    main()
