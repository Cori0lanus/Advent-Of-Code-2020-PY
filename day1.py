def sol1():
    lines = [int(line) for line in open('input/day1.txt', 'r').readlines()]

    for i in range(len(lines)):
        if lines.count(2020 - lines[i]) > 0:
            return lines[i] * (2020 - lines[i])


def sol2():
    lines = [int(line) for line in open('input/day1.txt', 'r').readlines()]

    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines.count(2020 - lines[i] - lines[j]) > 0:
                return lines[i] * lines[j] * (2020 - lines[i] - lines[j])
